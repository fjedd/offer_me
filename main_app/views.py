from __future__ import annotations

import django.contrib.auth as auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.shortcuts import render

from .models import JobOffer
from forms.add_offer_form import AddOfferForm
from forms.register_form import RegisterForm


def home(request):
    return render(request, 'main_app/home.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {user}')
            return redirect('login')
    return render(request, 'main_app/register.html', {'form': form})


def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = AuthenticationForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            messages.success(request, 'Logged in')
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid credentials')

    return render(request, 'main_app/login.html', {'form': form})


def logout(request):
    auth.logout(request)
    messages.success(request, 'Logged out')
    return redirect('home')


@login_required
def panel(request):
    return render(request, 'main_app/panel.html')


@login_required
def offer_form(request):
    form = AddOfferForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'Offer added')
                return redirect('offers')
    return render(request, 'main_app/offer_form.html', {'form': form})


def offers(request):
    job_offers = JobOffer.objects.all()
    return render(
        request, 'main_app/offers.html', {'job_offers': job_offers},
    )
