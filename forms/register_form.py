from __future__ import annotations

from django import forms
from django.contrib.auth.forms import UserCreationForm

from main_app.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name',
            'last_name', 'password1', 'password2',
        )
