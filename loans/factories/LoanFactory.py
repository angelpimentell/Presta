from factory.django import DjangoModelFactory
from ..models import Loan
from faker import Faker

from ..factories import ClientFactory
from ..factories import PaymentTimeFactory

fake = Faker()


class LoanFactory(DjangoModelFactory):
    client = ClientFactory()
    payment_time = PaymentTimeFactory()
    total_amount = fake.pydecimal(left_digits=9, right_digits=2, positive=True)
    due_amount = fake.pydecimal(left_digits=9, right_digits=2, positive=True)
    interests = fake.pydecimal(left_digits=3, right_digits=2, positive=True)
    fee_type = fake.random_int(min=0, max=3)
    start = fake.date_between()
    finish = fake.date_between()

    class Meta:
        model = Loan
