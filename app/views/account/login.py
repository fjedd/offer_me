from typing import Dict

import django.contrib.auth as auth
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import View

from app.decorators import user_not_authenticated
from forms.login_form import LoginForm


@method_decorator(user_not_authenticated, name="dispatch")
class LoginView(View):
    template_name: str = "app/account/login.html"
    redirect_url: str = "/"
    form_class = LoginForm

    def get(self, request) -> HttpResponse:
        return render(request, self.template_name, {"form": self.form_class})

    def post(self, request) -> HttpResponse:
        data: Dict[str, str] = request.POST
        username: str = data["username"]
        password: str = data["password"]
        user: User = auth.authenticate(username=username, password=password)
        if user:
            messages.success(request, "Logged in")
            auth.login(request, user)
            return redirect(self.redirect_url)
        else:
            messages.warning(request, "Invalid credentials")
            return render(request, "app/account/login.html", {"form": self.form_class})
