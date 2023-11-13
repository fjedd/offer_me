from django.test import Client, TestCase

from main_app.models import User


class AuthenticationTestCase(TestCase):
    def setUp(self):
        # Arrange
        self.client = Client()
        self.username = "test_username"
        self.password = "test_Password"
        self.email = "test@example.com"
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password,
            email=self.email,
        )

    def tearDown(self):
        self.user.delete()

    def test_login_correct_credentaials(self):
        # Act
        url = self.client.get("/login")
        user = self.client.login(
            username=self.username,
            password=self.password,
        )
        # Assert
        self.assertEqual(url.status_code, 200)
        self.assertTrue(user)

    def test_login_incorrect_credentials(self):
        # Act
        url = self.client.get("/login")
        user = self.client.login(username="wrong_user", password="wrong_pass")
        # Assert
        self.assertEqual(url.status_code, 200)
        self.assertFalse(user)

    def test_register_new_user(self):
        # Arrange
        path = "/register"
        user_data = {
            "username": "newUser",
            "password1": self.password,
            "password2": self.password,
            "email": "new@email.com",
        }
        # Act
        url = self.client.get(path)
        response = self.client.post(path, user_data)
        # Assert
        self.assertEqual(url.status_code, 200)
        self.assertEqual(response.status_code, 302)

    def test_register_existing_user(self):
        # Arrange
        path = "/register"
        user_data = {
            "username": self.username,
            "password1": self.password,
            "password2": self.password,
            "email": self.email,
        }
        # Act
        url = self.client.get(path)
        response = self.client.post(path, user_data)
        # Assert
        self.assertEqual(url.status_code, 200)
        self.assertContains(
            response,
            "A user with that username already exists.",
        )
