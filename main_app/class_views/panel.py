from django.views.generic import TemplateView


class UserPanelView(TemplateView):
    template_name = "main_app/panel.html"
