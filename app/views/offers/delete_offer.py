from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView

from app.decorators import user_can_modify
from app.mixins.login_required_mixin import LoginRequiredMixin
from app.models import JobOffer


@method_decorator(user_can_modify, name="dispatch")
class DeleteOfferView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = JobOffer
    template_name: str = "app/offers/delete_offer.html"
    success_url: str = "/offers"

    def get_success_message(self, cleaned_data: dict[str, str]) -> str:
        return f"{self.object.title} offer was deleted"
