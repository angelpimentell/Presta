import factory

from ..models.PaymentTime import PaymentTime

from faker import Faker

fake = Faker()


class PaymentTimeFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('name')
    measure_type = factory.Faker('random_int', min=0, max=3)
    quantity = factory.Faker('random_int', min=0, max=3)

    class Meta:
        model = PaymentTime
