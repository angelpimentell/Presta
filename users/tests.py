from django.test import TestCase
from .models import User


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(name="lion",
                            email="roar",
                            password="roar",
                            avatar="image.jpg",
                            description="roar")

        def test_animals_can_speak(self):
            lion = User.objects.get(name="lion")
            self.assertEqual(lion, 'The lion says "roar"')
