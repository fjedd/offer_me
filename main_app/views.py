from django.shortcuts import render, redirect
from django.contrib import messages

import django.contrib.auth as auth

from backend.forms.register_form import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import JobOffer


def home(request):
    return render(request, "main_app/home.html")


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
    return render(request, "main_app/register.html", {"form": form})


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

    return render(request, "main_app/login.html", {"form": form})


def logout(request):
    auth.logout(request)
    messages.success(request, "Logged out")
    return redirect("home")


@login_required
def panel(request):
    return render(request, "main_app/panel.html")


@login_required
def offer_form(request):
    return render(request, "main_app/offer.form.html")


def offers(request):
    job_offers = JobOffer.objects.all()
    return render(
        request, "main_app/offers.html", {"job_offers": job_offers}
    )
