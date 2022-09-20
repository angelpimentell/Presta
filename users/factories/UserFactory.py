from factory.django import DjangoModelFactory
from ..models import User
from faker import Faker

fake = Faker()


class UserFactory(DjangoModelFactory):
    rol = fake.random_int(min=0, max=3)
    name = fake.name()
    email = fake.email()
    password = fake.password(length=12)
    avatar = fake.file_path(depth=5, category='image')
    description = fake.text(max_nb_chars=100)

    class Meta:
        model = User
