from datetime import datetime

from django import forms
from django.test import TestCase

from lessons.forms import LessonCreateForm
from lessons.models import LessonRequest, Teacher, User


class TestLessonCreateForm(TestCase):
    fixtures_path = "lessons/tests/fixtures"
    fixtures = [
        f"{fixtures_path}/user_john.json", f"{fixtures_path}/lesson_request.json", f"{fixtures_path}/teacher.json"
    ]

    def setUp(self):
        self.user = User.objects.get(pk=1)
        self.teacher = Teacher.objects.get(pk=1)
        self.lesson_request = LessonRequest.objects.get(pk=1)

        self.form_input = {
            "datetime": datetime.now(),
            "teacher": self.teacher,
            "duration": 45,
            "further_information": "Hello, world!",
            "user": self.user,
            "lesson_request": self.lesson_request,
        }

    def test_form_has_correct_fields(self):
        form = LessonCreateForm()

        self.assertIn("datetime", form.fields)
        self.assertIn("teacher", form.fields)
        self.assertIn("duration", form.fields)
        self.assertIn("further_information", form.fields)
        self.assertIn("user", form.fields)
        self.assertIn("lesson_request", form.fields)

        datetime_field = form.fields["datetime"]
        user_field = form.fields["user"]
        lesson_request_field = form.fields["lesson_request"]
        duration_field = form.fields["duration"]

        self.assertTrue(isinstance(datetime_field.widget, forms.DateTimeInput))
        self.assertTrue(isinstance(user_field.widget, forms.HiddenInput))
        self.assertTrue(isinstance(lesson_request_field.widget, forms.HiddenInput))
        self.assertTrue(isinstance(duration_field.widget, forms.NumberInput))

    def test_form_accepts_valid_input_data(self):
        self._assert_form_is_valid()

    def _assert_form_is_valid(self):
        form = LessonCreateForm(self.form_input)

        self.assertTrue(form.is_valid())

    def _assert_form_is_invalid(self):
        form = LessonCreateForm(self.form_input)

        self.assertFalse(form.is_valid())