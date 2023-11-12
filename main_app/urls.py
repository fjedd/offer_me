from __future__ import annotations

from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('panel', views.panel, name='panel'),
    path('offers', views.offers, name='offers'),
    path('offer_form', views.offer_form, name='offer_form'),
    path('delete_offer/<str:pk>', views.delete_offer, name='delete_offer'),

]
