from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from lessons.forms import LessonCreateForm, LessonEditForm
from lessons.models import Lesson, LessonRequest
"""
Subpages for directors.
"""


def director_lesson_requests(request):
    return render(
        request, "administrator/lesson_requests.html", {
            "allowed_roles": ["Administrator", "Director"],
            "dashboard": {
                "heading": "Lesson Requests",
                "subheading": "View student lesson requests."
            }
        })


def director_manage_administrators(request):
    return render(
        request, "director/manage_administrators.html", {
            "allowed_roles": ["Director"],
            "dashboard": {
                "heading": "Administrator Accounts",
                "subheading": "View and manage administrator accounts"
            }
        })

def director_create_administrator(request):
    if request.method == "POST":
        form = AdministratorCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            return redirect("director")

    else:
        form = AdministratorCreationForm()

    return render(request, "director/manage_administrator/create_administrator.html", {
        "form": form,
        "allowed_roles": ["Director"]
    })

""" Views for deleting objects. """


class AdministratorLessonDeleteView(DeleteView):
    model = Lesson
    template_name = "delete.html"
    extra_context = {
        "allowed_roles": ["Administrator", "Director"],
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
        "allowed_roles": ["Administrator", "Director"],
        "dashboard": {
            "heading": "Modify lesson",
            "subheading": "Change details about this lesson."
        }
    }

    def get_success_url(self):
        return f"/administrator/lesson-requests/book/{self.object.lesson_request.pk}"


class AdministratorLessonCreateView(CreateView):
    model = Lesson
    form_class = LessonCreateForm
    template_name = "edit.html"
    extra_context = {
        "allowed_roles": ["Administrator", "Director"],
        "dashboard": {
            "heading": "Create new lesson",
            "subheading": "Create a new lesson by specifying details."
        }
    }

    def get_success_url(self):
        return f"/administrator/lesson-requests/book/{self.object.lesson_request.pk}"

    def get_initial(self):
        initial = super(AdministratorLessonCreateView, self).get_initial()

        lesson_request = LessonRequest.objects.filter(pk=self.kwargs["lesson_request_id"]).first()

        initial["lesson_request"] = lesson_request.pk
        initial["user"] = lesson_request.user.pk
        return initial
