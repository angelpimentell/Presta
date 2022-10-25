from django.test import TestCase

from ..factories.loan_factory import LoanFactory
from ..factories.payment_time_factory import PaymentTimeFactory
from ..factories.client_factory import ClientFactory


class LoanTestCase(TestCase):

    def test_new_loan(self):
        client = ClientFactory()
        loan_example = LoanFactory.create(clients=(client,))
        self.assertIsNotNone(loan_example)
