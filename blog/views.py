from django.views import generic

from .models import Author, Post


class AuthorListView(generic.ListView):
    model = Author
    template_name = "blog/author_list.html"
    context_object_name = "author_list"


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "post_list"

    
