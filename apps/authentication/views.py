from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
import django.contrib.auth as auth
from backend.forms.login_form import LoginForm
from backend.forms.register_form import RegisterForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def home(request):
    return render(request, "authentication/home.html")


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = UserCreationForm()
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, "User created")
        return redirect("login")

    return render(request, "authentication/register.html", {"form": form})


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user:
            messages.success(request, "Logged in")
            auth.login(request, user)
            return render(request, "authentication/panel.html", {"username": username})

        messages.error(request, "Bad credentils")
        return redirect("login")
    return render(request, "authentication/login.html", {"form": AuthenticationForm()})


def logout(request):
    auth.logout(request)
    messages.success(request, "Logged out")
    return redirect("home")


def panel(request):
    return render(request, "authentication/panel.html")
