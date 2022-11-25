from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

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
    return redirect("administrator/lesson-requests")

def director(request):
    return render(request, "user_dashboard.html", {"allowed_roles": ["Director"]})

"""
Subpages for students.
"""
def student_booked_lessons(request):
    return HttpResponse("Page does not exist yet.")

def student_lesson_requests(request):
    return HttpResponse("Page does not exist yet.")

def student_manage_dependents(request):
    return HttpResponse("Page does not exist yet.")

def student_transactions(request):
    return HttpResponse("Page does not exist yet.")

"""
Subpages for administrators.
"""
def administrator_lesson_requests(request):
    return render(request, "administrator/lesson_requests.html", {"allowed_roles": ["Administrator"], "dashboard": {"heading": "Lesson Requests", "subheading": "View student lesson requests."}})

def administrator_student_balances(request):
    return HttpResponse("Page does not exist yet.")

"""
Subpages for directors.
"""
def director_lesson_requests(request):
    return render(request, "administrator/lesson_requests.html", {"allowed_roles": ["Administrator"], "dashboard": {"heading": "Lesson Requests", "subheading": "View student lesson requests."}})

def director_student_balances(request):
    return HttpResponse("Page does not exist yet.")

def director_manage_administrators(request):
    return HttpResponse("Page does not exist yet.")