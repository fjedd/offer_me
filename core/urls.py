from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("app.urls.base_urls")),
    path("offers/", include("app.urls.offer_urls")),
    path("account/", include("app.urls.account_urls")),
]
