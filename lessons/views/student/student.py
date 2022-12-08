from django.shortcuts import redirect


def student(request):
    return redirect("student/lesson-requests")