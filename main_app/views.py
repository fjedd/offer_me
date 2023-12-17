import django.contrib.auth as auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from forms.login_form import LoginForm
from forms.offer_form import OfferForm
from forms.register_form import RegisterForm

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
    form = LoginForm()
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


@login_required(login_url="/")
def logout(request):
    auth.logout(request)
    messages.success(request, "Logged out")
    return redirect("home")


@login_required(login_url="/login")
def panel(request):
    return render(request, "main_app/panel.html")


def offers(request):
    job_offers = JobOffer.objects.all()
    return render(
        request,
        "main_app/offers.html",
        {"job_offers": job_offers},
    )


@login_required(login_url="/login")
def offer_form(request):
    form = OfferForm()
    if request.method == "POST":
        form = OfferForm(request.POST)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.author = request.user
            offer.save()
            messages.success(request, "Offer added")
            return redirect("offers")
    return render(request, "main_app/offer_form.html", {"form": form})


@login_required(login_url="/login")
def update_offer(request, pk):
    offer = get_object_or_404(JobOffer, id=pk)
    form = OfferForm(instance=offer)
    if offer.author == request.user:
        if request.method == "POST":
            form = OfferForm(request.POST, instance=offer)
            if form.is_valid():
                form.save()
                return redirect("offers")
    else:
        messages.warning(request, "You do not have permission to edit this offer")
        return redirect("offers")
    return render(request, "main_app/offer_form.html", {"form": form})


@login_required(login_url="/login")
def delete_offer(request, pk):
    offer = get_object_or_404(JobOffer, id=pk)
    if offer.author == request.user:
        if request.method == "POST":
            offer.delete()
            messages.success(request, f"{offer.title} offer was deleted")
            return redirect("offers")
    else:
        messages.warning(request, "You do not have permission to delete this offer")
        return redirect("offers")
    return render(request, "main_app/delete_offer.html", {"offer": offer})
