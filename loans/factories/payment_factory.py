import factory

from ..factories.loan_factory import LoanFactory
from ..factories.payment_time_factory import PaymentTimeFactory


class Payment(factory.django.DjangoModelFactory):
    loan = LoanFactory()
    payment_time = PaymentTimeFactory()
    amount = factory.Faker('pydecimal', left_digits=9, right_digits=2, positive=True)
    date = factory.Faker('date_between')
    delay = factory.Faker('random_int', min=0, max=365)
    interests = factory.Faker('pydecimal', left_digits=3, right_digits=2, positive=True)

    class Meta:
        model = 'loans.Payment'
