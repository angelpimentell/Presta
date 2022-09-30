import factory

from faker import Faker

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    rol = factory.Faker('random_int', min=0, max=3)
    name = factory.Faker('name')
    email = factory.Faker('email')
    password = factory.Faker('password', length=12)
    avatar = factory.Faker('file_path', depth=5, category='image')
    description = factory.Faker('text', max_nb_chars=100)

    class Meta:
        model = "users.User"
