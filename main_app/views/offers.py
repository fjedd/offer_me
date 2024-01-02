from django.views.generic import ListView

from ..models import JobOffer


class OffersView(ListView):
    model = JobOffer
    paginate_by: int = 10
    template_name: str = "main_app/offers.html"
    context_object_name: str = "job_offers"
