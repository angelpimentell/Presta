from django.test import TestCase

from ..factories.LoanFactory import LoanFactory


class LoanTestCase(TestCase):

    def test_new_loan(self):
        loan_example = LoanFactory()
        self.assertIsNotNone(loan_example)
