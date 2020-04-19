from django.conf.urls import url

from .views import (
    RedirectionView,
    HomeView,
    UserLoginView,
    UserLogoutView,
    UserCreationView,
)


urlpatterns = [
    url(r"^logout", UserLogoutView.as_view(), name="logout"),
    url(r"^login", UserLoginView.as_view(), name="login"),
    url(r"^register", UserCreationView.as_view(), name="register"),
    url(r"^(?P<slug>[-\w]+)", RedirectionView.as_view(), name="redirection"),
    url(r"^", HomeView.as_view(), name="home"),
]
