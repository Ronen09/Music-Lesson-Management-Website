from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from lessons.forms import LogInForm


def log_in(request):
    if request.method == "POST":
        form = LogInForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")

            user = authenticate(email=email, password=password)

            if user is not None:
                login(request, user)

                # Redirect user to appropriate user dashboard
                if (user.role == "Student"):
                    return redirect("student")
                elif (user.role == "Administrator"):
                    return redirect("administrator")
                elif (user.role == "Director"):
                    return redirect("director")

        messages.add_message(request, messages.ERROR, "The credentials provided were invalid!")

    form = LogInForm()

    return render(request, "log_in.html", {"form": form, "allowed_roles": ["Anonymous"]})
