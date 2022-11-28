from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic.edit import DeleteView, UpdateView, CreateView

from lessons.forms import SignUpForm, LogInForm, LessonRequestForm, LessonRequestsFilterForm, LessonEditForm, LessonRequestEditForm
from lessons.models import LessonRequest, Lesson

# Create your views here.


def lesson_request(request):
    if request.method == "POST":
        form = LessonRequestForm(request.POST, current_user=request.user)

        if form.is_valid():
            form.save()

            return redirect("home")
    else:
        form = LessonRequestForm(current_user=request.user)

    return render(request, "lesson_request.html", {
        "form": form,
        "allowed_roles": ["Student"]
    })


"""
Main 'site' pages (index page, log in, sign up and log out).
"""


def home(request):
    return render(request, "home.html", {"allowed_roles": ["Anonymous"]})


def log_in(request):
    if request.method == "POST":
        form = LogInForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")

            user = authenticate(email=email, password=password)

            if user is not None:
                login(request, user)

                # Redirect user to appropriate user dashboard
                if (user.role == "Student"):
                    return redirect("student")
                elif (user.role == "Administrator"):
                    return redirect("administrator")
                elif (user.role == "Director"):
                    return redirect("director")

        messages.add_message(request, messages.ERROR,
                             "The credentials provided were invalid!")

    form = LogInForm()

    return render(request, "log_in.html", {
        "form": form,
        "allowed_roles": ["Anonymous"]
    })


def log_out(request):
    logout(request)

    return redirect("home")


def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            # Redirect user to appropriate user dashboard
            if (user.role == "Student"):
                return redirect("student")
            elif (user.role == "Administrator"):
                return redirect("administrator")
            elif (user.role == "Director"):
                return redirect("director")
    else:
        form = SignUpForm()

    return render(request, "sign_up.html", {
        "form": form,
        "allowed_roles": ["Anonymous"]
    })


"""
User dashboards for each type of user (student, administrator and director).
"""


def student(request):
    return render(request, "user_dashboard.html",
                  {"allowed_roles": ["Student"]})


def administrator(request):
    return redirect("administrator/lesson-requests")


def director(request):
    return render(request, "user_dashboard.html",
                  {"allowed_roles": ["Director"]})


"""
Subpages for students.
"""


def student_booked_lessons(request):
    return HttpResponse("Page does not exist yet.")


def student_lesson_requests(request):
    return HttpResponse("Page does not exist yet.")


def student_manage_dependents(request):
    return HttpResponse("Page does not exist yet.")


def student_transactions(request):
    return HttpResponse("Page does not exist yet.")


"""
Subpages for administrators.
"""


def administrator_lesson_requests(request):
    # Get form
    if request.method == "POST":
        form = LessonRequestsFilterForm(request.POST)
    else:
        form = LessonRequestsFilterForm()

    # Generate correct list of requests to show
    lesson_requests = LessonRequest.objects.all()

    selected_student = form["student_filter"].value()
    selected_term = form["term_filter"].value()
    selected_status = form["status_filter"].value()

    if selected_student not in [None, ""]:
        lesson_requests = lesson_requests.filter(user=selected_student)

    if selected_status not in [None, "", "all"]:
        if selected_status == "fulfilled":
            lesson_requests = lesson_requests.filter(is_fulfilled=True)
        else:
            lesson_requests = lesson_requests.filter(is_fulfilled=False)

    def convert_lesson_request_to_card(lesson_request):
        heading = lesson_request.user
        no_of_lessons = str(lesson_request.no_of_lessons)
        lesson_duration = f"{lesson_request.lesson_duration_in_mins} minutes"
        lesson_interval = f"{lesson_request.lesson_interval_in_days} days"

        book_url = reverse('administrator/lesson-requests/book',
                           kwargs={"lesson_request_id": lesson_request.pk})
        view_url = reverse('administrator/lesson-requests/view',
                           kwargs={"lesson_request_id": lesson_request.pk})
        edit_url = reverse('administrator/lesson-requests/edit',
                           kwargs={"pk": lesson_request.pk})
        delete_url = reverse('administrator/lesson-requests/delete',
                             kwargs={"pk": lesson_request.pk})

        return {
            "heading":
            heading,
            "info": [{
                "title": "Number of Lessons",
                "description": no_of_lessons,
            }, {
                "title": "Lesson Duration",
                "description": lesson_duration,
            }, {
                "title": "Interval Between Lessons",
                "description": lesson_interval,
            }],
            "buttons": [{
                "name": "View",
                "url": view_url,
                "type": "outline-primary",
            }, {
                "name": "Book",
                "url": book_url,
                "type": "outline-primary",
            }, {
                "name": "Edit",
                "url": edit_url,
                "type": "outline-primary",
            }, {
                "name": "Delete",
                "url": delete_url,
                "type": "outline-danger",
            }],
        }

    cards = map(convert_lesson_request_to_card, lesson_requests)

    # Return page
    return render(
        request, "administrator/lesson_requests.html", {
            "allowed_roles": ["Administrator"],
            "lesson_requests": lesson_requests,
            "form": form,
            "dashboard": {
                "heading": "Lesson Requests",
                "subheading": "Fulfill and delete student lesson requests."
            },
            "cards": cards
        })


def administrator_lesson_requests_view(request, lesson_request_id):
    return render(
        request, "administrator/lesson_requests/view.html", {
            "allowed_roles": ["Administrator"],
            "dashboard": {
                "heading": f"View Lesson Request #{lesson_request_id}",
                "subheading": "See more details about this lesson request."
            },
            "lesson_request": LessonRequest.objects.get(pk=lesson_request_id),
        })


def administrator_lesson_requests_book(request, lesson_request_id):
    lesson_request = LessonRequest.objects.get(pk=lesson_request_id)

    # Get lessons for this lesson request (if they exist)
    lessons = Lesson.objects.filter(lesson_request=lesson_request)

    # Convert lessons to cards
    cards = []

    for lesson in lessons:
        edit_url = reverse("administrator/lesson-requests/book/lessons/edit",
                           kwargs={
                               "lesson_request_id": lesson_request.pk,
                               "pk": lesson.pk
                           })
        delete_url = reverse(
            "administrator/lesson-requests/book/lessons/delete",
            kwargs={
                "lesson_request_id": lesson_request.pk,
                "pk": lesson.pk
            })

        heading = lesson.datetime.strftime("%d %B %Y (%H:%M)")

        cards.append({
            "heading":
            heading,
            "info": [{
                "title": "Teacher",
                "description": lesson.teacher,
            }, {
                "title": "Duration",
                "description": f"{lesson.duration} minutes",
            }, {
                "title": "Further Information",
                "description": lesson.further_information,
            }],
            "buttons": [{
                "name": "Edit",
                "url": edit_url,
                "type": "outline-primary"
            }, {
                "name": "Delete",
                "url": delete_url,
                "type": "outline-danger",
            }]
        })

    return render(
        request, "administrator/lesson_requests/book.html", {
            "allowed_roles": ["Administrator"],
            "dashboard": {
                "heading":
                f"Book Lessons for Lesson Request #{lesson_request_id}",
                "subheading": "Book lessons for this lesson request."
            },
            "lesson_request": lesson_request,
            "cards": cards,
        })


def administrator_lesson_requests_book_finalise_booking(
        request, lesson_request_id):
    lesson_request = LessonRequest.objects.get(pk=lesson_request_id)
    lesson_request.is_fulfilled = True
    lesson_request.save()

    return redirect(f"/administrator/lesson-requests")


def administrator_lesson_requests_book_lessons_delete(request,
                                                      lesson_request_id,
                                                      lesson_id):
    lesson = Lesson.objects.get(pk=lesson_id)
    lesson.delete()

    return redirect(f"/administrator/lesson-requests/book/{lesson_request_id}")


def administrator_lesson_requests_delete(request, lesson_request_id):
    lesson_request = LessonRequest.objects.get(pk=lesson_request_id)
    lesson_request.delete()

    return redirect("administrator/lesson-requests")


def administrator_student_balances(request):
    return HttpResponse("Page does not exist yet.")


"""
Subpages for directors.
"""


def director_lesson_requests(request):
    return render(
        request, "administrator/lesson_requests.html", {
            "allowed_roles": ["Administrator"],
            "dashboard": {
                "heading": "Lesson Requests",
                "subheading": "View student lesson requests."
            }
        })


def director_student_balances(request):
    return HttpResponse("Page does not exist yet.")


def director_manage_administrators(request):
    return HttpResponse("Page does not exist yet.")


""" Views for deleting objects. """


class AdministratorLessonRequestDeleteView(DeleteView):
    model = LessonRequest
    success_url = "/administrator/lesson-requests"
    template_name = "delete.html"
    extra_context = {
        "allowed_roles": ["Administrator"],
        "dashboard": {
            "heading": "Delete lesson request",
            "subheading": "Confirm deletion of lesson request."
        }
    }


class AdministratorLessonDeleteView(DeleteView):
    model = Lesson
    template_name = "delete.html"
    extra_context = {
        "allowed_roles": ["Administrator"],
        "dashboard": {
            "heading": "Delete lesson",
            "subheading": "Confirm deletion of lesson."
        }
    }

    def get_success_url(self):
        return f"/administrator/lesson-requests/book/{self.object.lesson_request.pk}"


class AdministratorLessonUpdateView(UpdateView):
    model = Lesson
    form_class = LessonEditForm
    template_name = "edit.html"
    extra_context = {
        "allowed_roles": ["Administrator"],
        "dashboard": {
            "heading": "Modify lesson",
            "subheading": "Change details about this lesson."
        }
    }

    def get_success_url(self):
        return f"/administrator/lesson-requests/book/{self.object.lesson_request.pk}"


class AdministratorLessonCreateView(CreateView):
    model = Lesson
    form_class = LessonEditForm
    template_name = "edit.html"
    extra_context = {
        "allowed_roles": ["Administrator"],
        "dashboard": {
            "heading": "Create new lesson",
            "subheading": "Create a new lesson by specifying details."
        }
    }

    def get_success_url(self):
        return f"/administrator/lesson-requests/book/{self.object.lesson_request.pk}"

    def get_initial(self):
        initial = super(AdministratorLessonCreateView, self).get_initial()

        lesson_request = LessonRequest.objects.filter(
            pk=self.kwargs["lesson_request_id"]).first()

        initial["lesson_request"] = lesson_request.pk
        initial["user"] = lesson_request.user.pk
        return initial


class AdministratorLessonRequestUpdateView(UpdateView):
    model = LessonRequest
    form_class = LessonRequestEditForm
    success_url = "/administrator/lesson-requests"
    template_name = "edit.html"
    extra_context = {
        "allowed_roles": ["Administrator"],
        "dashboard": {
            "heading": "Modify lesson request",
            "subheading": "Change details about this lesson request."
        }
    }