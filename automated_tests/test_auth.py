import string
from random import choice
from typing import Dict

import pytest
from playwright.sync_api import Page, expect


def test_login(client: Page):
    client.get_by_test_id("login-button").click()
    client.get_by_label("Username").fill("testuser1")
    client.get_by_label("Password").fill("test_password")
    client.get_by_role("button", name="Login").click()
    expect(client.locator(".alert")).to_contain_text("Logged in")


def test_login_user_logged_in(client: Page, logged_in_state):
    expect(client.get_by_test_id("login-button")).not_to_be_visible()
    client.goto("/account/login")
    client.wait_for_url("/")


def test_logout(client: Page, logged_in_state):
    client.get_by_test_id("user-dropdown").click()
    client.get_by_test_id("logout-button").click()
    expect(client.locator(".alert")).to_contain_text("Logged out")


def test_logout_user_not_logged(client: Page):
    expect(client.get_by_test_id("user-dropdown")).not_to_be_visible()
    expect(client.get_by_test_id("logout-button")).not_to_be_visible()


@pytest.mark.skip(reason="Disabled for pipeline purpose")
def test_register_correct_data(client: Page):
    data: Dict[str, str] = {
        "username": "".join(choice(string.ascii_letters) for i in range(10)),
        "password": "testPass123",
        "email": "test@example.com",
        "first_name": "Test name",
        "last_name": "Test",
    }
    client.get_by_test_id("register-button").click()
    client.get_by_placeholder("Username").fill(data["username"])
    client.get_by_placeholder("Email").fill(data["email"])
    client.get_by_placeholder("First name").fill(data["first_name"])
    client.get_by_placeholder("Last name").fill(data["last_name"])
    client.locator("[name='password1']").fill(data["password"])
    client.locator("[name='password2']").fill(data["password"])
    client.get_by_role("button", name="Register account").click()
    print(client.content())
    expect(client.locator(".alert")).to_contain_text(
        f"Account created for {data['username']}"
    )


@pytest.mark.parametrize(
    "data, expected_message",
    (
        (
            {
                "username": "Test User",
                "password1": "testPass123",
                "password2": "testPass123",
                "email": "test@example.com",
                "first_name": "Test name",
                "last_name": "Test",
            },
            "Enter a valid username",
        ),
        (
            {
                "username": "testtest_username",
                "password1": "testPass123",
                "password2": "testPass1234",
                "email": "test@example.com",
                "first_name": "Test name",
                "last_name": "Test",
            },
            "The two password fields didn’t match",
        ),
        (
            {
                "username": "testtest_username",
                "password1": "password",
                "password2": "password",
                "email": "test@example.com",
                "first_name": "Test name",
                "last_name": "Test",
            },
            "This password is too common",
        ),
        (
            {
                "username": "testtest_username",
                "password1": "passwor",
                "password2": "passwor",
                "email": "test@example.com",
                "first_name": "Test name",
                "last_name": "Test",
            },
            "This password is too short. It must contain at least 8 characters",
        ),
    ),
)
def test_register_incorrect_data(client: Page, data: Dict[str, str], expected_message):
    client.get_by_test_id("register-button").click()
    client.get_by_placeholder("Username").fill(data["username"])
    client.get_by_placeholder("Email").fill(data["email"])
    client.get_by_placeholder("First name").fill(data["first_name"])
    client.get_by_placeholder("Last name").fill(data["last_name"])
    client.locator("[name='password1']").fill(data["password1"])
    client.locator("[name='password2']").fill(data["password2"])
    client.get_by_role("button", name="Register account").click()

    expect(client.locator("//ul[@class='errorlist']/li")).to_contain_text(
        expected_message
    )


def test_register_user_logged_in(client: Page, logged_in_state):
    expect(client.get_by_test_id("logout-button")).not_to_be_visible()
    client.goto("/account/register")
    client.wait_for_url("/")
