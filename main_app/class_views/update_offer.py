from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from decorators.decorators import user_is_author
from forms.offer_form import OfferForm

from ..models import JobOffer


@method_decorator(user_is_author, name="dispatch")
class UpdateOfferView(LoginRequiredMixin, UpdateView):
    model = JobOffer
    form_class = OfferForm
    template_name: str = "main_app/offer_form.html"
    success_url: str = "/offers"
