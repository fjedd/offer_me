from typing import Dict

import pytest
from django.core import mail
from django.core.mail.message import EmailMessage
from django.urls import reverse
from lxml import html

from core.settings import EMAIL_HOST_USER

register_url: str = reverse("register")
reset_password_url: str = reverse("password_reset")

FROM_EMAIL: str = EMAIL_HOST_USER or "webmaster@localhost"


@pytest.mark.django_db
def test_register_email(client):
    user_data: Dict[str, str] = {
        "username": "new_test_user",
        "email": "new_test@example.com",
        "first_name": "Test",
        "last_name": "User",
        "password1": "test_password",
        "password2": "test_password",
    }
    expected_data: Dict[str, str] = {
        "subject": "Offer Me Account registered",
        "from_email": FROM_EMAIL,
        "to_email": user_data["email"],
        "link_url": "http://testserver/account/login",
    }
    # Act
    client.post(register_url, user_data)
    email: EmailMessage = mail.outbox[0]
    email_body: html.HtmlElement = html.fromstring(email.body)
    # Assert
    assert len(mail.outbox) == 1
    assert email.subject == expected_data["subject"]
    assert email.from_email == expected_data["from_email"]
    assert email.to[0] == expected_data["to_email"]
    assert (
        email_body.get_element_by_id("loginLink").get("href")
        == "http://testserver/account/login"
    )


def test_password_reset_email(client, users):
    post_data: Dict[str, str] = {"email": users[0].email}
    expected_data: Dict[str, str] = {
        "subject": "Password reset request",
        "from_email": FROM_EMAIL,
        "to_email": users[0].email,
        "link_url": "http://testserver/account/login",
    }
    # Act
    client.post(reset_password_url, post_data)
    email: EmailMessage = mail.outbox[0]
    email_body: html.HtmlElement = html.fromstring(email.body)
    # Assert
    assert len(mail.outbox) == 1
    assert email.subject == expected_data["subject"]
    assert email.from_email == expected_data["from_email"]
    assert email.to[0] == expected_data["to_email"]
    assert (
        "http://testserver/account/password-reset-confirm/"
        in email_body.get_element_by_id("passwordResetLink").get("href")
    )
