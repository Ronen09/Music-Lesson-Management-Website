from django.shortcuts import redirect


def director(request):
    return redirect("administrator/lesson-requests")