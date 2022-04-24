from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import get_user_model
from customauth.forms import RegisterForm



class RegisterView(generic.CreateView):
    model = get_user_model()
    form_class = RegisterForm
    template_name = "customauth/register.html"
    success_url = reverse_lazy("blog:author-list")
