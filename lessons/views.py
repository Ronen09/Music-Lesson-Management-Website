from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from lessons.forms import SignUpForm, LogInForm, LessonRequestForm

# Create your views here.
def lesson_request(request):
    if request.method == "POST":
        form = LessonRequestForm(request.POST, current_user=request.user)

        if form.is_valid():
            form.save()

            return redirect("home")
    else:
        form = LessonRequestForm(current_user=request.user)

    return render(
        request, "lesson_request.html", {"form": form, "allowed_roles": ["Student"]}
    )


"""
Main 'site' pages (index page, log in, sign up and log out).
"""
def home(request):
    return render(request, "home.html", {"allowed_roles": ["Anonymous"]})

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
                if (user.role == "Student"): return redirect("student")
                elif (user.role == "Administrator"): return redirect("administrator")
                elif (user.role == "Director"): return redirect("director")

        messages.add_message(
            request, messages.ERROR, "The credentials provided were invalid!"
        )

    form = LogInForm()

    return render(
        request, "log_in.html", {"form": form, "allowed_roles": ["Anonymous"]}
    )

def log_out(request):
    logout(request)

    return redirect("home")

def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            # Redirect user to appropriate user dashboard
            if (user.role == "Student"): return redirect("student")
            elif (user.role == "Administrator"): return redirect("administrator")
            elif (user.role == "Director"): return redirect("director")
    else:
        form = SignUpForm()

    return render(
        request, "sign_up.html", {"form": form, "allowed_roles": ["Anonymous"]}
    )

"""
User dashboards for each type of user (student, administrator and director).
"""
def student(request):
    return render(request, "user_dashboard.html", {"allowed_roles": ["Student"]})

def administrator(request):
    return render(request, "user_dashboard.html", {"allowed_roles": ["Administrator"], "dashboard": {"heading": "Lesson Requests", "subheading": "View student lesson requests."}})

def director(request):
    return render(request, "user_dashboard.html", {"allowed_roles": ["Director"]})