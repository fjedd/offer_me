from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name: str = "main_app/home.html"
