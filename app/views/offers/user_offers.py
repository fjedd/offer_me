from app.mixins.login_required_mixin import LoginRequiredMixin
from app.models import JobOffer

from .offers import OffersView


class UserOffersView(LoginRequiredMixin, OffersView):
    def get_queryset(self):
        return JobOffer.objects.filter(author=self.request.user)
