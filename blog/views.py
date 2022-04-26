from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

from .mixins import EachUserPassesTestMixin, EachAuthorPassesTestMixin
from .forms import AuthorForm, PostForm
from .models import Author, Post


class AuthorListView(generic.ListView):
    model = Author


class AuthorDetailView(generic.DetailView):
    model = Author


class AuthorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy("blog:author-list")

    def dispatch(self, request, *args, **kwargs):
        try:
            if (Author.objects.get(user=request.user)):
                messages.warning(request, "You already have an author account.")
                return redirect("blog:post-list")                
        except ObjectDoesNotExist:
            pass
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        return super().form_valid(form)


class AuthorUpdateView(LoginRequiredMixin, 
                       EachUserPassesTestMixin,
                       generic.UpdateView):
    model = Author
    form_class = AuthorForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self) -> str:
        self.success_url = reverse("blog:author-detail", kwargs={'pk': self.object.id})
        return super().get_success_url()


class PostListView(generic.ListView):
    model = Post


class PostDetailView(generic.DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin,
                     generic.CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user.author
        return super().form_valid(form)

    def get_success_url(self) -> str:
        self.success_url = reverse("blog:post-detail", kwargs={'pk': self.object.id})
        return super().get_success_url()


class PostUpdateView(LoginRequiredMixin,
                     EachAuthorPassesTestMixin,
                     generic.UpdateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user.author
        return super().form_valid(form)

    def get_success_url(self) -> str:
        self.success_url = reverse("blog:post-detail", kwargs={'pk': self.object.id})
        return super().get_success_url()


class PostDeleteView(LoginRequiredMixin,
                     EachAuthorPassesTestMixin,
                     generic.DeleteView):
    model = Post
    success_url = reverse_lazy("blog:post-list")
