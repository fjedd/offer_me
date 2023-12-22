from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from decorators.decorators import user_is_author
from forms.offer_form import OfferForm

from ..models import JobOffer


@method_decorator(user_is_author, name="dispatch")
class UpdateOfferView(LoginRequiredMixin, UpdateView):
    model = JobOffer
    template_name = "main_app/offer_form.html"
    form_class = OfferForm
    success_url = "/offers"
