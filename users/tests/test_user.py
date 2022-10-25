from django.test import TestCase
from users.factories.user_factory import UserFactory

import factory

class UserTestCase(TestCase):
    def test_new_user(self):
        user_example = factory.SubFactory(UserFactory)
        self.assertIsNotNone(user_example)
