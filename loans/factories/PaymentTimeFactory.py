import factory

from faker import Faker

fake = Faker()


class PaymentTimeFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('name')
    measure_type = factory.Faker('random_int', min=0, max=3)
    quantity = factory.Faker('random_int', min=0, max=3)

    class Meta:
        model = 'loans.PaymentTime'
