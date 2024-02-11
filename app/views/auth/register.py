from typing import Dict

from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import EmailMessage
from django.http.response import HttpResponse
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

from core import settings
from forms.register_form import RegisterForm

from ...decorators import user_not_authenticated


@method_decorator(user_not_authenticated, name="dispatch")
class RegisterView(SuccessMessageMixin, CreateView):
    form_class = RegisterForm
    template_name: str = "app/auth/register.html"
    success_url: str = "login"
    email_from = settings.EMAIL_HOST_USER

    def get_success_message(self, cleaned_data: dict[str, str]) -> str:
        return f"Account created for {cleaned_data['username']}"

    def form_valid(self, form: RegisterForm) -> HttpResponse:
        data: Dict[str, str] = form.cleaned_data
        context: Dict[str, str] = {
            "username": data["username"],
            "referer": self.request.META.get("HTTP_ORIGIN", ""),
        }
        email: EmailMessage = EmailMessage(
            subject="Offer Me Account registered",
            body=render_to_string("emails/new_user_email.html", context=context),
            from_email=self.email_from,
            to=[data["email"]],
        )
        email.content_subtype = "html"
        email.send()
        return super().form_valid(form)
