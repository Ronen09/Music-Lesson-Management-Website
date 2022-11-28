"""msms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from lessons import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("lesson_request/", views.lesson_request, name="lesson_request"),

    # General site pages
    path("", views.home, name="home"),
    path("login/", views.log_in, name="log_in"),
    path("logout/", views.log_out, name="log_out"),
    path("signup/", views.sign_up, name="sign_up"),

    # User dashboards
    path("student/", views.student, name="student"),
    path("administrator/", views.administrator, name="administrator"),
    path("director/", views.director, name="director"),

    # Subpages for student dashboard
    path("student/booked-lessons",
         views.student_booked_lessons,
         name="student/booked-lessons"),
    path("student/lesson-requests",
         views.student_lesson_requests,
         name="student/lesson-requests"),
    path("student/manage-dependents",
         views.student_manage_dependents,
         name="student/manage-dependents"),
    path("student/transactions",
         views.student_transactions,
         name="student/transactions"),

    # Subpages for administrator dashboard
    path("administrator/lesson-requests",
         views.administrator_lesson_requests,
         name="administrator/lesson-requests"),
    path("administrator/lesson-requests/view/<int:lesson_request_id>",
         views.administrator_lesson_requests_view,
         name="administrator/lesson-requests/view"),
    path("administrator/lesson-requests/book/<int:lesson_request_id>",
         views.administrator_lesson_requests_book,
         name="administrator/lesson-requests/book"),
    path(
        "administrator/lesson-requests/book/<int:lesson_request_id>/finalise-booking",
        views.administrator_lesson_requests_book_finalise_booking,
        name="administrator/lesson-requests/book/finalise-booking"),
    path("administrator/lesson-requests/delete/<int:lesson_request_id>",
         views.administrator_lesson_requests_delete,
         name="administrator/lesson-requests/delete"),
    path(
        "administrator/lesson-requests/book/<int:lesson_request_id>/lessons/delete/<int:lesson_id>",
        views.administrator_lesson_requests_book_lessons_delete,
        name="administrator/lesson-requests/book/lessons/delete"),
    path("administrator/student-balances",
         views.administrator_student_balances,
         name="administrator/student-balances"),

    # Subpages for director dashboard
    path("director/lesson-requests",
         views.director_lesson_requests,
         name="director/lesson-requests"),
    path("director/student-balances",
         views.director_student_balances,
         name="director/student-balances"),
    path("director/manage-administrators",
         views.director_manage_administrators,
         name="director/manage-administrators"),
]