from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

from decorators.decorators import user_not_authenticated
from forms.register_form import RegisterForm


@method_decorator(user_not_authenticated, name="dispatch")
class RegisterView(SuccessMessageMixin, CreateView):
    template_name = "main_app/register.html"
    form_class = RegisterForm
    success_url = "login"

    def get_success_message(self, cleaned_data: dict[str, str]) -> str:
        return f"Account created for {cleaned_data['username']}"
