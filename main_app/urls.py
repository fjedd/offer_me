from django.urls import path

from .class_views import (delete_offer, home, login, logout, offer_form,
                          offers, panel, register, update_offer)

urlpatterns = [
    path("", home.HomeView.as_view(), name="home"),
    path("login", login.LoginView.as_view(), name="login"),
    path("register", register.RegisterView.as_view(), name="register"),
    path("logout", logout.LogoutView.as_view(), name="logout"),
    path("panel", panel.UserPanelView.as_view(), name="panel"),
    path("offers", offers.OffersView.as_view(), name="offers"),
    path("offer_form", offer_form.OfferFormView.as_view(), name="offer_form"),
    path(
        "delete_offer/<str:pk>",
        delete_offer.DeleteOfferView.as_view(),
        name="delete_offer",
    ),
    path(
        "update_offer/<str:pk>",
        update_offer.UpdateOfferView.as_view(),
        name="update_offer",
    ),
]
