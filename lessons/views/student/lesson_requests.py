from django.shortcuts import render
from django.urls import reverse

from lessons.forms import LessonRequestsFilterForm
from lessons.models import LessonRequest


def lesson_requests(request):
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

        view_url = reverse('administrator/lesson-requests/view', kwargs={"lesson_request_id": lesson_request.pk})
        edit_url = reverse('administrator/lesson-requests/edit', kwargs={"pk": lesson_request.pk})
        delete_url = reverse('administrator/lesson-requests/delete', kwargs={"pk": lesson_request.pk})

        # Check if the lesson request has been fulfilled
        has_lesson_request_been_fulfilled(lesson_request)

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
        request, "student/lesson_requests.html", {
            "allowed_roles": ["Student"],
            "lesson_requests": lesson_requests,
            "form": form,
            "dashboard": {
                "heading": "Lesson Requests",
                "subheading": "Fulfill and delete your lesson requests."
            },
            "cards": cards
        })
