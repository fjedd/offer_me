from django.urls import path

from .views import (
    delete_offer,
    home,
    offer_form,
    offers,
    panel,
    search_offers,
    update_offer,
    user_offers,
)
from .views.auth import login, logout, register
from .views.auth.password_reset import (
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)

urlpatterns = [
    path("", home.HomeView.as_view(), name="home"),
    path("login", login.LoginView.as_view(), name="login"),
    path("register", register.RegisterView.as_view(), name="register"),
    path("logout", logout.LogoutView.as_view(), name="logout"),
    path("panel", panel.UserPanelView.as_view(), name="panel"),
    path("offers", offers.OffersView.as_view(), name="offers"),
    path("user_offers", user_offers.UserOffersView.as_view(), name="user_offers"),
    path("search", search_offers.SearchOffersView.as_view(), name="search_offers"),
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
    path("password-reset/", PasswordResetView.as_view(), name="password_reset"),
    path(
        "password-reset/sent/",
        PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete/",
        PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
