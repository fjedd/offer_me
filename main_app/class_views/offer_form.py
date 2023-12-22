from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import CreateView

from forms.offer_form import OfferForm


class OfferFormView(LoginRequiredMixin, CreateView):
    template_name = "main_app/offer_form.html"
    form_class = OfferForm

    def form_valid(self, form) -> HttpResponse:
        offer = form.save(commit=False)
        offer.author = self.request.user
        offer.save()
        messages.success(self.request, "Offer added")
        return redirect("offers")
