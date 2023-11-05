from __future__ import annotations

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class AuthenticationTestCase(TestCase):
    # TODO add tests

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'testuser@example.com',
        }
        self.user = User.objects.create_user(**self.user_data)

    def tearDown(self):
        pass

    def test_register_new_user(self):
        pass

    def register_existing_user(self):
        pass

    def login_correct_credentaials(self):
        pass

    def login_incorrect_credentials(self):
        pass
