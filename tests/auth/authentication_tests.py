from typing import Dict

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse

login_url: str = reverse("login")
logout_url: str = reverse("logout")
register_url: str = reverse("register")


def test_login_correct_credentials(client, users):
    # Arrange
    user_data: Dict[str:str] = {
        "username": users[0].username,
        "password": "test_password",
    }
    # Act
    user_logged: client = client.login(**user_data)
    # Assert
    assert user_logged is True


def test_login_wrong_credentials(client, users):
    # Arrange
    user_data: Dict[str:str] = {"username": "asdf", "password": "asdfpass"}
    # Act
    user_logged: client = client.login(**user_data)
    # Assert
    assert user_logged is False


def test_register_new_user(client, users):
    # Arrange
    user_data: Dict[str, str] = {
        "username": "new_test_user",
        "email": "new_test@example.com",
        "first_name": "Test",
        "last_name": "User",
        "password1": "test_password",
        "password2": "test_password",
    }
    expected_message: str = f"Account created for {user_data['username']}"
    # Act
    response: Dict[str, str] = client.post(register_url, user_data, follow=True)
    # Assert
    assert expected_message in str(response.content)
    assert User.objects.get(username=user_data["username"])


def test_register_existing_user(client, users):
    # Arrange
    user_data: Dict[str, str] = {
        "username": "test_user",
        "email": "test@example.com",
        "first_name": "Test",
        "last_name": "User",
        "password1": "test_password",
        "password2": "test_password",
    }
    expected_message: str = "A user with that username already exists."
    user_count: int = User.objects.all().count()
    # Act
    response: HttpResponse = client.post(register_url, user_data, follow=True)
    # Assert
    assert expected_message in str(response.content)
    assert User.objects.all().count() == user_count


def test_logout_logged_user(client, users):
    # Arrange
    user_data: Dict[str:str] = {
        "username": users[0].username,
        "password": "test_password",
    }
    expected_message: str = "Logged out"
    # Act
    client.login(**user_data)
    response: HttpResponse = client.get(logout_url, follow=True)
    # Assert
    assert expected_message in str(response.content)
