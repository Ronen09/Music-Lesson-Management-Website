from django.test import TestCase

from lessons.forms.shared import LessonRequestEditForm


class TestLessonRequestEditForm(TestCase):

    def setUp(self):
        self.form_input = {
            "no_of_lessons": 5,
            "lesson_duration_in_mins": 45,
            "lesson_interval_in_days": 7,
            "further_information": "Hello, world!"
        }

    def test_form_has_correct_fields(self):
        form = LessonRequestEditForm()

        self.assertIn("no_of_lessons", form.fields)
        self.assertIn("lesson_duration_in_mins", form.fields)
        self.assertIn("lesson_interval_in_days", form.fields)
        self.assertIn("further_information", form.fields)

    def test_no_of_lessons_cannot_be_zero(self):
        self.form_input["no_of_lessons"] = 0
        self._assert_form_is_invalid()

    def test_no_of_lessons_cannot_be_negative(self):
        self.form_input["no_of_lessons"] = -5
        self._assert_form_is_invalid()

    def test_lesson_duration_in_mins_cannot_be_zero(self):
        self.form_input["lesson_duration_in_mins"] = 0
        self._assert_form_is_invalid()

    def test_lesson_duration_in_mins_cannot_be_negative(self):
        self.form_input["lesson_duration_in_mins"] = -45
        self._assert_form_is_invalid()

    def test_lesson_interval_in_days_cannot_be_zero(self):
        self.form_input["lesson_interval_in_days"] = 0
        self._assert_form_is_invalid()

    def test_lesson_interval_in_days_cannot_be_negative(self):
        self.form_input["lesson_interval_in_days"] = -45
        self._assert_form_is_invalid()

    def test_further_information_can_be_none(self):
        self.form_input["further_information"] = None
        self._assert_form_is_valid()

    def test_form_accepts_valid_input_data(self):
        self._assert_form_is_valid()

    def _assert_form_is_valid(self):
        form = LessonRequestEditForm(self.form_input)

        self.assertTrue(form.is_valid())

    def _assert_form_is_invalid(self):
        form = LessonRequestEditForm(self.form_input)

        self.assertFalse(form.is_valid())