from django.contrib.auth.mixins import LoginRequiredMixin as BaseLoginRequiredMixin


class LoginRequiredMixin(BaseLoginRequiredMixin):
    redirect_field_name = None
