from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class UserPanelView(LoginRequiredMixin, TemplateView):
    template_name: str = "main_app/panel.html"
