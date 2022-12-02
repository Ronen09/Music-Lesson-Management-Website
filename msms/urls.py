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
from django.urls import include, path

from lessons import views
from lessons.views import *

main_patterns = [
    path("", views.home, name="home"),
    path("login/", views.log_in, name="log_in"),
    path("logout/", views.log_out, name="log_out"),
    path("signup/", views.sign_up, name="sign_up"),
    path("admin/", admin.site.urls),
    path("student/", views.student, name="student"),
    path("administrator/", views.administrator, name="administrator"),
    path("director/", views.director, name="director"),
    path("lesson_request/", views.lesson_request, name="lesson_request"),
]

student_patterns = [
    path("booked-lessons", views.student_booked_lessons, name="student/booked-lessons"),
    path("lesson-requests", views.student_lesson_requests, name="student/lesson_requests"),
    path("delete-lesson-request/<int:id>", views.student_delete_lesson_requests, name="student/delete_lesson_request"),
    path("edit-lesson-request/<int:id>", views.student_edit_lesson_requests, name="student/edit_lesson_request"),
    path("manage-dependents/", views.student_manage_dependents, name="student/manage-dependents"),
    path("transactions/", views.student_transactions, name="student/transactions"),
]

administrator_patterns = [
    path("lesson-requests", views.administrator_lesson_requests, name="administrator/lesson-requests"),
    path("lesson-requests/view/<int:lesson_request_id>",
         views.administrator_lesson_requests_view,
         name="administrator/lesson-requests/view"),
    path("lesson-requests/book/<int:lesson_request_id>",
         views.administrator_lesson_requests_book,
         name="administrator/lesson-requests/book"),
    path("lesson-requests/book/<int:lesson_request_id>/finalise-booking",
         views.administrator_lesson_requests_book_finalise_booking,
         name="administrator/lesson-requests/book/finalise-booking"),
    path("lesson-requests/delete/<pk>",
         AdministratorLessonRequestDeleteView.as_view(),
         name="administrator/lesson-requests/delete"),
    path("lesson-requests/edit/<pk>",
         AdministratorLessonRequestUpdateView.as_view(),
         name="administrator/lesson-requests/edit"),
    path("lesson-requests/book/<int:lesson_request_id>/lessons/delete/<pk>",
         AdministratorLessonDeleteView.as_view(),
         name="administrator/lesson-requests/book/lessons/delete"),
    path("lesson-requests/book/<int:lesson_request_id>/lessons/edit/<pk>",
         AdministratorLessonUpdateView.as_view(),
         name="administrator/lesson-requests/book/lessons/edit"),
    path("lesson-requests/book/<int:lesson_request_id>/lessons/create",
         AdministratorLessonCreateView.as_view(),
         name="administrator/lesson-requests/book/lessons/create"),
    path("student-balances", views.administrator_student_balances, name="administrator/student-balances"),
]

director_patterns = [
    path("lesson-requests", views.director_lesson_requests, name="director/lesson-requests"),
    path("student-balances", views.director_student_balances, name="director/student-balances"),
    path("manage-administrators", views.director_manage_administrators, name="director/manage-administrators"),
]

urlpatterns = [
    path("", include(main_patterns)),
    path("student/", include(student_patterns)),
    path("administrator/", include(administrator_patterns)),
    path("director/", include(director_patterns)),
]