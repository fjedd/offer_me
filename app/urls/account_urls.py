from django.urls import path

from app.views.account import login, logout, panel, register
from app.views.account.password_reset import (
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)

urlpatterns = [
    path("login", login.LoginView.as_view(), name="login"),
    path("register", register.RegisterView.as_view(), name="register"),
    path("logout", logout.LogoutView.as_view(), name="logout"),
    path("panel", panel.UserPanelView.as_view(), name="panel"),
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
