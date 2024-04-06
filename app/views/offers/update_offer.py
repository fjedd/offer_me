from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from app.decorators import user_can_modify
from app.mixins.login_required_mixin import LoginRequiredMixin
from app.models import JobOffer
from forms.offer_form import OfferForm


@method_decorator(user_can_modify, name="dispatch")
class UpdateOfferView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = JobOffer
    form_class = OfferForm
    template_name: str = "app/offers/offer_form.html"
    success_url: str = "/offers"
    success_message: str = "Offer updated"
