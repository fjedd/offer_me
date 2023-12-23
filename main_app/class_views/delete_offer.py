from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView

from decorators.decorators import user_is_author

from ..models import JobOffer


@method_decorator(user_is_author, name="dispatch")
class DeleteOfferView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = JobOffer
    template_name: str = "main_app/delete_offer.html"
    success_url: str = "/offers"

    def get_success_message(self, cleaned_data: dict[str, str]) -> str:
        return f"{self.object.title} offer was deleted"
