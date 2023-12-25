from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from decorators.decorators import user_can_modify
from forms.offer_form import OfferForm

from ..models import JobOffer


@method_decorator(user_can_modify, name="dispatch")
class UpdateOfferView(LoginRequiredMixin, UpdateView):
    model = JobOffer
    form_class = OfferForm
    template_name: str = "main_app/offer_form.html"
    success_url: str = "/offers"
