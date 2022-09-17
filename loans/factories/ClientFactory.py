from factory.django import DjangoModelFactory
from ..models import Client
from faker import Faker

fake = Faker()


class ClientFactory(DjangoModelFactory):
    email = fake.email()
    direction = fake.address()
    telephone_number = fake.random_int(min=100000000, max=999999999)
    telephone_ext = fake.random_int(min=10, max=99)
    avatar = fake.file_path(depth=5, category='image')
    description = fake.text(max_nb_chars=100)

    class Meta:
        model = Client
