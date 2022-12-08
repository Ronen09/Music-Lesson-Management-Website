from django.shortcuts import redirect


def administrator(request):
    return redirect("administrator/lesson-requests")