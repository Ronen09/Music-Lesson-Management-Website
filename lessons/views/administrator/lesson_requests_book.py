from django.shortcuts import render
from django.urls import reverse

from lessons.models import Lesson, LessonRequest


def lesson_requests_book(request, lesson_request_id):
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
        delete_url = reverse("administrator/lesson-requests/book/lessons/delete",
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
            }, {
                "title": "Price",
                "description": get_lesson_price(lesson),
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
            "allowed_roles": ["Administrator", "Director"],
            "dashboard": {
                "heading": f"Book Lessons for Lesson Request #{lesson_request_id}",
                "subheading": "Book lessons for this lesson request."
            },
            "lesson_request": lesson_request,
            "cards": cards,
        })