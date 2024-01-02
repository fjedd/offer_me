from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import CreateView

from forms.offer_form import OfferForm
from main_app.models import JobOffer


class OfferFormView(LoginRequiredMixin, CreateView):
    form_class = OfferForm
    template_name: str = "main_app/offer_form.html"

    def form_valid(self, form) -> HttpResponse:
        offer: JobOffer = form.save(commit=False)
        offer.author = self.request.user
        offer.save()
        messages.success(self.request, "Offer added")
        return redirect("offers")
