from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from .mixins import (
    AuthorMatchTestMixin, UserMatchTestMixin, 
    HasAuthorAccountTestMixin,
)

from .forms import AuthorForm, PostForm, PostSearchForm
from .models import Author, Post


class AuthorListView(generic.ListView):
    model = Author


class AuthorDetailView(generic.DetailView):
    model = Author


class AuthorCreateView(LoginRequiredMixin, 
                       HasAuthorAccountTestMixin, 
                       generic.CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy("blog:author-list")
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        return super().form_valid(form)


class AuthorUpdateView(LoginRequiredMixin, 
                       UserMatchTestMixin,
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


class PostSearchListView(generic.ListView):
    template_name = "blog/post_search_list.html"
    context_object_name = "post_search_list"
    model = Post

    def get_queryset(self):
        self.queryset = self.model.objects.search(key_string=self.kwargs["key_string"])
        return super().get_queryset()


class PostFromAuthorListView(generic.ListView):
    template_name = "blog/posts_from_author.html"
    context_object_name = "posts_from_author"
    model = Post

    def get_queryset(self):
        self.queryset = self.model.objects.filter(author=self.kwargs["author_pk"])
        return super().get_queryset()
    

class PostListView(generic.edit.FormMixin, generic.ListView):
    model = Post
    form_class = PostSearchForm

    def get_success_url(self) -> str:
        return reverse("blog:post-search-list", kwargs={
            "key_string": self.get_form().data.get("key_string")
        })

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


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
                     AuthorMatchTestMixin,
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
                     AuthorMatchTestMixin,
                     generic.DeleteView):
    model = Post
    success_url = reverse_lazy("blog:post-list")
