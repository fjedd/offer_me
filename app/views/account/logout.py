import django.contrib.auth as auth
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import View

from app.mixins.login_required_mixin import LoginRequiredMixin


class LogoutView(LoginRequiredMixin, View):
    def get(self, request) -> HttpResponse:
        auth.logout(request)
        messages.success(request, "Logged out")
        return redirect("home")
