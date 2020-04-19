from django.views.generic import DetailView, CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Link
from .utils import generate_slug
from .forms import CreateLinkForm
from users.forms import LoginForm, CustomUserCreationForm


class RedirectionView(LoginRequiredMixin, DetailView):
    model = Link
    slug_field = "slug"

    def dispatch(self, request, *args, **kwargs):
        link = self.get_object()
        link.counter += 1
        link.save()
        return HttpResponseRedirect(link.original_url)


class HomeView(LoginRequiredMixin, CreateView):
    model = Link
    form_class = CreateLinkForm
    template_name = "shortener/index.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.original_url = form.cleaned_data["original_url"]
        form.instance.slug = generate_slug()
        form.instance.creator = self.request.user
        form.instance.save()
        messages.success(self.request, "Short URL was created")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["links"] = Link.objects.filter(creator=self.request.user)
        return context


class UserLoginView(LoginView):
    redirect_authenticated_user = True
    authentication_form = LoginForm
    template_name = "shortener/login.html"


class UserLogoutView(LogoutView):
    next_page = reverse_lazy("login")


class UserCreationView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("home")
    template_name = "shortener/register.html"

    def form_valid(self, form):
        valid = super(UserCreationView, self).form_valid(form)
        username, password = (
            form.cleaned_data.get("username"),
            form.cleaned_data.get("password1"),
        )
        new_user = authenticate(username=username, password=password)
        if new_user is not None:
            login(self.request, new_user)
        else:
            messages.info(self.request, "Incorrect registration")
        return valid
