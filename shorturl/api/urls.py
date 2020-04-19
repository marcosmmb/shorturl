from django.urls import include, path

urlpatterns = [
    path('registration/', include("rest_auth.registration.urls")),
    path('auth/', include("rest_auth.urls")),
]