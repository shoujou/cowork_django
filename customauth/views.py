from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import get_user_model
from customauth.forms import RegisterForm
from django.contrib.auth import authenticate, login


class RegisterView(generic.CreateView):
    model = get_user_model()
    form_class = RegisterForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("blog:author-create")

    def get_success_url(self) -> str:
        login(self.request, self.object)
        return super().get_success_url()
