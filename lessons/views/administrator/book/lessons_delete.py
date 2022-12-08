from django.shortcuts import redirect

from lessons.models import Lesson


def lessons_delete(request, lesson_request_id, lesson_id):
    lesson = Lesson.objects.get(pk=lesson_id)
    lesson.delete()

    return redirect(f"/administrator/lesson-requests/book/{lesson_request_id}")