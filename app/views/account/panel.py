from django.views.generic import TemplateView

from app.mixins.login_required_mixin import LoginRequiredMixin


class UserPanelView(LoginRequiredMixin, TemplateView):
    template_name: str = "app/panel.html"
