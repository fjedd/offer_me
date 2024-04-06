from django.urls import path

from app.views import home

urlpatterns = [
    path("", home.HomeView.as_view(), name="home"),
]
