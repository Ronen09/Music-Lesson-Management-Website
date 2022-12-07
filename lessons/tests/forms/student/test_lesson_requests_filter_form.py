from django.test import TestCase

from lessons.forms.student import LessonRequestsFilterForm
from lessons.models import Term


class TestLessonRequestsFilterForm(TestCase):
    fixtures_path = "lessons/tests/fixtures"
    fixtures = [f"{fixtures_path}/term.json"]

    def setUp(self):
        self.term = Term.objects.get(pk=1)

        self.form_input = {
            "term_filter": self.term,
            "status_filter": "All",
        }

    def test_form_has_correct_fields(self):
        form = LessonRequestsFilterForm()

        self.assertIn("term_filter", form.fields)
        self.assertIn("status_filter", form.fields)

    def test_form_accepts_valid_input_data(self):
        self._assert_form_is_valid()

    def _assert_form_is_valid(self):
        form = LessonRequestsFilterForm(self.form_input)

        self.assertTrue(form.is_valid())

    def _assert_form_is_invalid(self):
        form = LessonRequestsFilterForm(self.form_input)

        self.assertFalse(form.is_valid())