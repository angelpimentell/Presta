from django.test import TestCase
from ..factories.UserFactory import UserFactory


class UserTestCase(TestCase):
    def test_new_user(self):
        user_example = UserFactory()
        self.assertIsNotNone(user_example)
