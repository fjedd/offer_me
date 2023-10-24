from django.shortcuts import render, redirect
from django.contrib import messages

import django.contrib.auth as auth
from static.data import offers_data

from backend.forms.register_form import RegisterForm
from django.contrib.auth.forms import AuthenticationForm


def home(request):
    return render(request, "authentication/home.html")


def register(request):
    if request.user.is_authenticated:
        return redirect("home")
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {user}")
            return redirect("login")
    return render(request, "authentication/register.html", {"form": form})


def login(request):
    if request.user.is_authenticated:
        return redirect("home")
    form = AuthenticationForm()
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            messages.success(request, "Logged in")
            auth.login(request, user)
            return redirect("home")
        else:
            messages.info(request, "Invalid credentials")

    return render(request, "authentication/login.html", {"form": form})


def logout(request):
    auth.logout(request)
    messages.success(request, "Logged out")
    return redirect("home")


def panel(request):
    return render(request, "authentication/panel.html")


def offers(request):
    return render(
        request, "authentication/offers.html", {"job_offers": offers_data.job_offers}
    )
