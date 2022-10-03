import factory

from faker import Faker

fake = Faker()


class ClientFactory(factory.django.DjangoModelFactory):
    email = factory.Faker('email')
    direction = factory.Faker('address')
    telephone_number = factory.Faker('random_int', min=100000000, max=999999999)
    telephone_ext = factory.Faker('random_int', min=10, max=99)
    avatar = factory.Faker('file_path', depth=5, category='image')
    description = factory.Faker('text', max_nb_chars=100)

    class Meta:
        model = 'loans.Client'
