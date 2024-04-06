from django.contrib.auth.forms import PasswordResetForm as BasePasswordResetForm
from django.contrib.auth.forms import SetPasswordForm


class PasswordResetForm(BasePasswordResetForm):
    class Meta:
        fields = "email"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Email"}
        )


class PasswordChangeForm(SetPasswordForm):
    class Meta:
        fields = ("new_password1", "new_password2")

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["new_password1"].widget.attrs.update(
            {"class": "form-control", "placeholder": "New password"}
        )
        self.fields["new_password2"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Confirm new password"}
        )
        self.fields["new_password2"].label = "Confirm new password"
