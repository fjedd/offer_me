import django.contrib.auth as auth
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import View


class LogoutView(LoginRequiredMixin, View):
    def get(self, request) -> HttpResponse:
        auth.logout(request)
        messages.success(request, "Logged out")
        return redirect("home")
