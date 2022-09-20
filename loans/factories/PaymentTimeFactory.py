from factory.django import DjangoModelFactory

from ..models.PaymentTime import PaymentTime

from faker import Faker

fake = Faker()


class PaymentTimeFactory(DjangoModelFactory):
    name = fake.name()
    measure_type = fake.random_int(min=0, max=3)
    quantity = fake.random_int(min=0, max=3)

    class Meta:
        model = PaymentTime
