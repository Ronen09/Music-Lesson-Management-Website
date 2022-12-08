from django.shortcuts import redirect, render

from lessons.forms import LessonRequestForm
from lessons.models import LessonRequest


def edit_lesson_requests(request, id):
    lesson_request = LessonRequest.objects.get(id=id)
    if request.user.is_authenticated:
        form = LessonRequestForm(current_user=request.user, instance=lesson_request)
        if request.method == 'POST':
            form = LessonRequestForm(request.POST, instance=lesson_request)
            if form.is_valid():
                form.save()
                return redirect("student/lesson_requests")
        lesson_request.delete()
    return render(request, "lesson_request.html", {"form": form, "allowed_roles": ["Student"]})