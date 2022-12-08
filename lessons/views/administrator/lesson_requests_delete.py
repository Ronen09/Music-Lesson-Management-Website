from django.shortcuts import redirect

from lessons.models import LessonRequest


def lesson_requests_delete(request, lesson_request_id):
    lesson_request = LessonRequest.objects.get(pk=lesson_request_id)
    lesson_request.delete()

    return redirect("administrator/lesson-requests")