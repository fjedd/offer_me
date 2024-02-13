from django.contrib.auth.views import (
    PasswordResetCompleteView as BasePasswordResetCompleteView,
)
from django.contrib.auth.views import (
    PasswordResetConfirmView as BasePasswordResetConfirmView,
)
from django.contrib.auth.views import PasswordResetDoneView as BasePasswordResetDoneView
from django.contrib.auth.views import PasswordResetView as BasePasswordResetView
from django.utils.decorators import method_decorator

from app.decorators import user_not_authenticated
from forms.password_reset_form import PasswordChangeForm, PasswordResetForm


@method_decorator(user_not_authenticated, name="dispatch")
class PasswordResetView(BasePasswordResetView):
    template_name = "app/auth/password_reset_form.html"
    form_class = PasswordResetForm
    html_email_template_name = "emails/password_reset_email.html"
    subject_template_name = "emails/password_reset_subject.txt"


@method_decorator(user_not_authenticated, name="dispatch")
class PasswordResetConfirmView(BasePasswordResetConfirmView):
    form_class = PasswordChangeForm
    template_name = "app/auth/password_reset_confirm.html"


@method_decorator(user_not_authenticated, name="dispatch")
class PasswordResetCompleteView(BasePasswordResetCompleteView):
    template_name = "app/auth/password_reset_complete.html"


@method_decorator(user_not_authenticated, name="dispatch")
class PasswordResetDoneView(BasePasswordResetDoneView):
    template_name = "app/auth/password_reset_done.html"
