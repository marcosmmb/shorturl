from django.urls import include, path
from django.conf.urls import url

from .views import CreateShortUrl

urlpatterns = [
    url(r"^shortener", CreateShortUrl.as_view(), name="shortener-create"),
    path("registration/", include("rest_auth.registration.urls")),
    path("auth/", include("rest_auth.urls")),
]
