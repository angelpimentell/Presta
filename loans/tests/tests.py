from django.test import TestCase
from ..factories import LoanFactory


class UserTestCase(TestCase):
    def test_new_loan(self):
        loan_example = LoanFactory()
        self.assertIsNotNone(loan_example)
