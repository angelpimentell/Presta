from django.test import TestCase

from ..factories.LoanFactory import LoanFactory
from ..factories.PaymentTimeFactory import PaymentTimeFactory
from ..factories.ClientFactory import ClientFactory


class LoanTestCase(TestCase):

    def test_new_loan(self):
        client = ClientFactory()
        loan_example = LoanFactory.create(clients=(client,))
        self.assertIsNotNone(loan_example)
