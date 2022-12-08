from django.shortcuts import redirect

from lessons.models import Invoice, LessonRequest


def finalise_booking(request, lesson_request_id):
    lesson_request = LessonRequest.objects.get(pk=lesson_request_id)
    lesson_request.is_fulfilled = True
    lesson_request.save()

    if Invoice.objects.filter(lesson_request=lesson_request, user=lesson_request.user).exists() == False:
        invoice = Invoice.objects.create(lesson_request=lesson_request, user=lesson_request.user)
        invoice.save()

    return redirect(f"/administrator/lesson-requests")