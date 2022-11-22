from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from lessons.forms import SignUpForm, LogInForm, LessonRequestForm

# Create your views here.
def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect("home")
    else:
        form = SignUpForm()

    return render(request, "sign_up.html", {"form": form})


def log_in(request):
    if request.method == "POST":
        form = LogInForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")

            user = authenticate(email=email, password=password)

            if user is not None:
                login(request, user)

                return redirect("home")

        messages.add_message(
            request, messages.ERROR, "The credentials provided were invalid!"
        )

    form = LogInForm()

    return render(request, "log_in.html", {"form": form})


def log_out(request):
    logout(request)

    return redirect("home")


def lesson_request(request):
    if request.method == "POST":
        form = LessonRequestForm(request.POST)

        if form.is_valid():
            lesson_request = form.save()

            return redirect("home")
    else:
        form = LessonRequestForm()

    return render(request, "lesson_request.html", {"form": form})


def home(request):
    return render(request, "home.html")
