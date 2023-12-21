from django.views.generic import ListView

from ..models import JobOffer


class OffersView(ListView):
    model = JobOffer
    template_name = "main_app/offers.html"
    context_object_name = "job_offers"
