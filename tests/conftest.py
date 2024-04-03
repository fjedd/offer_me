from typing import Dict, List

import pytest
from django.contrib.auth.models import Permission
from django.test import Client

from app.models import JobOffer, User


@pytest.fixture
def client() -> Client:
    return Client()


@pytest.fixture
def users(db) -> List[User]:
    """
    Prepare example users for testing
    """
    user_data = [
        {
            "username": "test_user",
            "email": "test@gmail.com",
            "first_name": "Test",
            "last_name": "User",
            "password": "test_password",
        },
        {
            "username": "user2",
            "email": "test2@gmail.com",
            "first_name": "Second",
            "last_name": "User",
            "password": "test_password",
        },
        {
            "username": "moderator_user",
            "email": "moderator@gmail.com",
            "first_name": "Moderator",
            "last_name": "User",
            "password": "test_password",
        },
    ]

    users: List[User] = [User.objects.create_user(**data) for data in user_data]
    perm: Permission = Permission.objects.get(codename="change_joboffer")
    users[2].user_permissions.add(perm)
    return users


@pytest.fixture
def offers(db, users) -> JobOffer:
    """
    Prepare example offers for testing
    """
    offers_data: List[Dict[str, str]] = [
        {
            "author": users[0],
            "title": "Software Engineer",
            "company": "Tech Innovators",
            "location": "San Francisco",
            "is_remote": "Hybrid",
            "salary": "120 000",
            "description": (
                "Exciting opportunity for a skilled software engineer to join our"
                " dynamic team."
            ),
            "url": "https://example.com/software-engineer",
        },
        {
            "author": users[1],
            "title": "Data Scientist",
            "company": "Data Insights Co.",
            "location": "New York",
            "is_remote": "Remote",
            "salary": "100 000",
            "description": (
                "Seeking a talented data scientist to drive innovation in data analysis"
                " and modeling."
            ),
            "url": "https://example.com/data-scientist",
        },
    ]
    return JobOffer.objects.bulk_create([JobOffer(**data) for data in offers_data])
