from django.contrib.auth.mixins import LoginRequiredMixin

from ..models import JobOffer
from .offers import OffersView


class UserOffersView(LoginRequiredMixin, OffersView):
    def get_queryset(self):
        return JobOffer.objects.filter(author=self.request.user)
