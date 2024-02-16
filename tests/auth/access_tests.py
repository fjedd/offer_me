from django.http import HttpResponse
from django.urls import reverse

login_url: str = reverse("login")
logout_url: str = reverse("logout")


def test_offer_form_user_not_logged(client):
    # Act
    response: HttpResponse = client.get(reverse("offer_form"))
    # Assert
    assert response.status_code == 302
    assert response.url == login_url


def test_panel_user_not_logged(client):
    # Act
    response: HttpResponse = client.get(reverse("panel"))
    # Assert
    assert response.status_code == 302
    assert response.url == login_url


def test_user_offers_user_not_logged(client):
    # Act
    response: HttpResponse = client.get(reverse("user_offers"))
    # Assert
    assert response.status_code == 302
    assert response.url == login_url


def test_logout_not_logged(client):
    # Act
    response: HttpResponse = client.get(logout_url)
    # Assert
    assert response.status_code == 302
    assert response.url == login_url
