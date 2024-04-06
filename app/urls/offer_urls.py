from django.urls import path

from app.views.offers import (
    delete_offer,
    offer_form,
    offers,
    search_offers,
    update_offer,
    user_offers,
)

urlpatterns = [
    path("", offers.OffersView.as_view(), name="offers"),
    path("my-offers", user_offers.UserOffersView.as_view(), name="user_offers"),
    path("search", search_offers.SearchOffersView.as_view(), name="search_offers"),
    path("form", offer_form.OfferFormView.as_view(), name="offer_form"),
    path(
        "delete/<str:pk>",
        delete_offer.DeleteOfferView.as_view(),
        name="delete_offer",
    ),
    path(
        "update/<str:pk>",
        update_offer.UpdateOfferView.as_view(),
        name="update_offer",
    ),
]
