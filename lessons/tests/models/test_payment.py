from django.core.exceptions import ValidationError
from django.test import TestCase

from lessons.models import Invoice, Payment, User


class TestPayment(TestCase):
    fixtures_path = "lessons/tests/fixtures"
    fixtures = [f"{fixtures_path}/invoice.json", f"{fixtures_path}/teacher.json", f"{fixtures_path}/payment.json"]

    def setUp(self):
        self.payment = Payment.objects.get(pk=1)

    def test_valid_payment(self):
        self._assert_payment_is_valid()

    def test_user_cannot_be_none(self):
        self.payment.user = None
        self._assert_payment_is_invalid()

    def test_invoice_cannot_be_none(self):
        self.payment.invoice = None
        self._assert_payment_is_invalid()

    def test_amount_paid_cannot_be_none(self):
        self.payment.invoice = None
        self._assert_payment_is_invalid()

    def test_amount_paid_cannot_zero(self):
        self.payment.amount_paid = 0
        self._assert_payment_is_invalid()

    def test_amount_paid_cannot_be_negative(self):
        self.payment.amount_paid = -1
        self._assert_payment_is_invalid()

    def test_amount_paid_cannot_have_more_than_two_decimal_places(self):
        self.payment.amount_paid = 1.234
        self._assert_payment_is_invalid()

    def _assert_payment_is_valid(self):
        try:
            self.payment.full_clean()
        except ValidationError:
            self.fail("Test payment should be valid.")

    def _assert_payment_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.payment.full_clean()