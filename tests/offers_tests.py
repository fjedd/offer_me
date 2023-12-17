from typing import Dict, Tuple

import pytest
from django.http import HttpResponse
from django.urls import reverse

from main_app.models import JobOffer

form_url: str = "offer_form"
delete_url: str = "delete_offer"
update_url: str = "update_offer"


def test_add_offer_authenticated_user(client, users):
    # Arrange
    user_data: Dict[str:str] = {
        "username": users[0].username,
        "password": "test_password",
    }
    offer_data: Dict[str, str] = {
        "title": "Test Offer",
        "company": "Test Company",
        "location": "Warsaw",
        "is_remote": "Hybrid",
        "salary": "240,000 USD",
        "description": "Exciting opportunity for a skilled software engineer to join our dynamic team.",
        "url": "https://example.com/software-engineer",
    }
    url: str = reverse(form_url)
    expected_message: str = "Offer added"
    offers_count: int = JobOffer.objects.all().count()
    # Act
    client.login(**user_data)
    response: HttpResponse = client.post(url, data=offer_data, follow=True)
    offer = JobOffer.objects.get()
    # Assert
    assert expected_message in str(response.content)
    assert JobOffer.objects.all().count() == offers_count + 1
    for key, expected_value in offer_data.items():
        assert getattr(offer, key) == expected_value


def test_add_offer_not_authenticated_user(client, users):
    # Arrange
    offer_data: Dict[str, str] = {
        "title": "Test Offer",
        "company": "Test Company",
        "location": "Warsaw",
        "is_remote": "Hybrid",
        "salary": "240,000 USD",
        "description": "Exciting opportunity for a skilled software engineer to join our dynamic team.",
        "url": "https://example.com/software-engineer",
    }
    url: str = reverse(form_url)
    expected_redirect: Tuple[str, int] = ("/login?next=/offer_form", 302)
    offers_count: int = JobOffer.objects.all().count()
    # Act
    response: HttpResponse = client.post(url, data=offer_data, follow=True)
    # Assert
    assert response.redirect_chain[0] == expected_redirect
    assert JobOffer.objects.all().count() == offers_count


def test_delete_offer_user_is_author(client, users, offers):
    # Arrange
    offer_id = offers[0].id
    user_data: Dict[str:str] = {
        "username": users[0].username,
        "password": "test_password",
    }
    url: str = reverse(delete_url, kwargs={"pk": offer_id})
    expected_message: str = (
        f"{JobOffer.objects.get(id=offer_id).title} offer was deleted"
    )
    offers_count: int = JobOffer.objects.all().count()
    # Act
    client.login(**user_data)
    response: HttpResponse = client.post(url, follow=True)
    # Assert
    assert expected_message in str(response.content)
    assert JobOffer.objects.all().count() == offers_count - 1
    with pytest.raises(JobOffer.DoesNotExist):
        JobOffer.objects.get(id=offer_id).exists()


def test_delete_offer_user_not_author(client, users, offers):
    # Arrange
    offer_id = offers[1].id
    user_data: Dict[str:str] = {
        "username": users[0].username,
        "password": "test_password",
    }
    url: str = reverse(delete_url, kwargs={"pk": offer_id})
    expected_message: str = "You do not have permission to delete this offer"
    offers_count: int = JobOffer.objects.all().count()
    # Act
    client.login(**user_data)
    response: HttpResponse = client.post(url, follow=True)
    # Assert
    assert expected_message in str(response.content)
    assert JobOffer.objects.all().count() == offers_count
    assert JobOffer.objects.get(id=offer_id)


def test_update_offer_user_is_author(client, users, offers):
    # Arrange
    offer_id = offers[0].id
    user_data: Dict[str:str] = {
        "username": users[0].username,
        "password": "test_password",
    }
    update_data: Dict[str, str] = {
        "author": users[0],
        "title": "Python Developer",
        "company": "Big City",
        "location": "Warsaw",
        "is_remote": "Hybrid",
        "salary": "240,000 USD",
        "description": "Exciting opportunity for a skilled software engineer to join our dynamic team.",
        "url": "https://example.com/software-engineer",
    }
    url: str = reverse(update_url, kwargs={"pk": offer_id})
    offers_count: int = JobOffer.objects.all().count()
    # Act
    client.login(**user_data)
    client.post(url, data=update_data, follow=True)
    offer: JobOffer = JobOffer.objects.get(id=offer_id)
    # Assert
    assert JobOffer.objects.all().count() == offers_count
    for key, expected_value in update_data.items():
        assert getattr(offer, key) == expected_value


def test_update_offer_user_not_author(client, users, offers):
    # Arrange
    offer_id = offers[1].id
    user_data: Dict[str:str] = {
        "username": users[0].username,
        "password": "test_password",
    }
    url: str = reverse(update_url, kwargs={"pk": offer_id})
    expected_message: str = "You do not have permission to edit this offer"
    offers_count: int = JobOffer.objects.all().count()
    # Act
    client.login(**user_data)
    response: HttpResponse = client.post(url, follow=True)
    # Assert
    assert JobOffer.objects.all().count() == offers_count
    assert expected_message in str(response.content)
