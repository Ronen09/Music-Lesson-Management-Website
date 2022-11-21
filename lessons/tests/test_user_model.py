from django.test import TestCase
from django.core.exceptions import ValidationError

from lessons.models import User


class TestUserModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            "johndoe@example.org", password="Password123"
        )

    def test_valid_user(self):
        self._assert_user_is_valid()

    def test_email_cannot_be_blank(self):
        self.user.email = ""

        self._assert_user_is_invalid()

    def test_email_must_be_unique(self):
        User.objects.create_user("janedoe@example.org", password="Password123")

        self.user.email = "janedoe@example.org"

        self._assert_user_is_invalid()

    def test_is_student_is_false_by_default(self):
        self.assertFalse(self.user.is_student)

    def _assert_user_is_valid(self):
        try:
            self.user.full_clean()
        except ValidationError:
            self.fail("Test user should be valid.")

    def _assert_user_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.user.full_clean()
