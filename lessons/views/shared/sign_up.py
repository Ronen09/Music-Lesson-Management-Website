from django.contrib.auth import login
from django.shortcuts import redirect, render

from lessons.forms import SignUpForm


def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            # Redirect user to appropriate user dashboard
            if (user.role == "Student"):
                return redirect("student")
            elif (user.role == "Administrator"):
                return redirect("administrator")
            elif (user.role == "Director"):
                return redirect("director")
    else:
        form = SignUpForm()

    return render(request, "sign_up.html", {"form": form, "allowed_roles": ["Anonymous"]})
