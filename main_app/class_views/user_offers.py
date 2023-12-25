from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from ..models import JobOffer


class UserOffersView(LoginRequiredMixin, ListView):
    model = JobOffer
    template_name: str = "main_app/offers.html"
    context_object_name: str = "job_offers"

    def get_queryset(self):
        return JobOffer.objects.filter(author=self.request.user)
