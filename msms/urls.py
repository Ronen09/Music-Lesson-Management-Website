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

from lessons import old_views
from lessons.views import administrator, director, shared, student

main_patterns = [
    path("", shared.home, name="home"),
    path("login/", shared.log_in, name="log_in"),
    path("logout/", shared.log_out, name="log_out"),
    path("signup/", shared.sign_up, name="sign_up"),
    path("admin/", admin.site.urls),
    path("student/", student.student, name="student"),
    path("administrator/", administrator.administrator, name="administrator"),
    path("director/", director.director, name="director"),
]

student_lesson_requests_patterns = [
    path("", student.lesson_requests, name="student/lesson-requests"),
    path("view/<int:lesson_request_id>", shared.view_lesson_request, name="student/lesson-requests/view"),
    path("edit/<pk>", shared.LessonRequestUpdateView.as_view(), name="student/lesson-requests/edit"),
    path("delete/<pk>", shared.LessonRequestDeleteView.as_view(), name="student/lesson-requests/delete"),
    path("view-lessons/<int:lesson_request_id>", student.view_lessons, name="student/lesson-requests/view-lessons"),
    path("lesson_request/", student.lesson_request, name="student/lesson-request"),
]

student_patterns = [
    path("booked-lessons", student.booked_lessons, name="student/booked-lessons"),
    path("lesson-requests/", include(student_lesson_requests_patterns)),
    path("invoices/", student.invoices, name="student/invoices"),
]

administrator_lesson_requests_patterns = [
    path("", administrator.lesson_requests, name="administrator/lesson-requests"),
    path("view/<int:lesson_request_id>", shared.view_lesson_request, name="administrator/lesson-requests/view"),
    path("book/<int:lesson_request_id>", administrator.lesson_requests_book, name="administrator/lesson-requests/book"),
    path("book/<int:lesson_request_id>/finalise-booking",
         administrator.book.finalise_booking,
         name="administrator/lesson-requests/book/finalise-booking"),
    path("delete/<pk>", shared.LessonRequestDeleteView.as_view(), name="administrator/lesson-requests/delete"),
    path("edit/<pk>", shared.LessonRequestUpdateView.as_view(), name="administrator/lesson-requests/edit"),
    path("book/<int:lesson_request_id>/lessons/delete/<pk>",
         old_views.AdministratorLessonDeleteView.as_view(),
         name="administrator/lesson-requests/book/lessons/delete"),
    path("book/<int:lesson_request_id>/lessons/edit/<pk>",
         old_views.AdministratorLessonUpdateView.as_view(),
         name="administrator/lesson-requests/book/lessons/edit"),
    path("book/<int:lesson_request_id>/lessons/create",
         old_views.AdministratorLessonCreateView.as_view(),
         name="administrator/lesson-requests/book/lessons/create"),
]

administrator_patterns = [
    path("lesson-requests/", include(administrator_lesson_requests_patterns)),
    path("student-balances", administrator.student_balances, name="administrator/student-balances"),
]

director_patterns = [
    path("lesson-requests", old_views.director_lesson_requests, name="director/lesson-requests"),
    path("student-balances", administrator.student_balances, name="director/student-balances"),
    path("manage-administrators", old_views.director_manage_administrators, name="director/manage-administrators"),
]

urlpatterns = [
    path("", include(main_patterns)),
    path("student/", include(student_patterns)),
    path("administrator/", include(administrator_patterns)),
    path("director/", include(director_patterns)),
]