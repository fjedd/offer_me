from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from app.mixins.login_required_mixin import LoginRequiredMixin
from forms.offer_form import OfferForm

from ..decorators import user_can_modify
from ..models import JobOffer


@method_decorator(user_can_modify, name="dispatch")
class UpdateOfferView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = JobOffer
    form_class = OfferForm
    template_name: str = "app/offer_form.html"
    success_url: str = "/offers"
    success_message: str = "Offer updated"
