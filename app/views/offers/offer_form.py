from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import CreateView

from app.mixins.login_required_mixin import LoginRequiredMixin
from app.models import JobOffer
from forms.offer_form import OfferForm


class OfferFormView(LoginRequiredMixin, CreateView):
    form_class = OfferForm
    template_name: str = "app/offers/offer_form.html"

    def form_valid(self, form) -> HttpResponse:
        offer: JobOffer = form.save(commit=False)
        offer.author = self.request.user
        offer.save()
        messages.success(self.request, "Offer added")
        return redirect("offers")
