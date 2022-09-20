from factory.django import DjangoModelFactory

from ..models.Payment import Payment
from ..factories.LoanFactory import LoanFactory
from ..factories.PaymentTimeFactory import PaymentTimeFactory

from faker import Faker

fake = Faker()


class Payment(DjangoModelFactory):
    loan = LoanFactory()
    payment_time = PaymentTimeFactory()
    amount = fake.pydecimal(left_digits=9, right_digits=2, positive=True)
    date = fake.date_between()
    delay = fake.random_int(min=0, max=365)
    interests = fake.pydecimal(left_digits=3, right_digits=2, positive=True)

    class Meta:
        model = Payment
