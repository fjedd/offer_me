from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

from forms.register_form import RegisterForm

from ..decorators import user_not_authenticated


@method_decorator(user_not_authenticated, name="dispatch")
class RegisterView(SuccessMessageMixin, CreateView):
    form_class = RegisterForm
    template_name: str = "main_app/register.html"
    success_url: str = "login"

    def get_success_message(self, cleaned_data: dict[str, str]) -> str:
        return f"Account created for {cleaned_data['username']}"
