from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

from .forms import AuthorForm
from .models import Author, Post


class AuthorListView(generic.ListView):
    model = Author
    context_object_name = "author_list"


class AuthorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy("blog:author-list")

    def get(self, request, *args, **kwargs):
        try:
            if (Author.objects.get(user=request.user)):
                return redirect("blog:post-list")                
        except ObjectDoesNotExist:
            pass
        return super().get(request, *args, **kwargs)
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        return super().form_valid(form)



class AuthorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy("blog:author-detail")

    def get_form(self, form_class):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(user=self.request.user, **self.get_form_kwargs())

class PostListView(generic.ListView):
    model = Post
    context_object_name = "post_list"


