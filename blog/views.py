#from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from blog.models import Post


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class PostListView(generic.ListView):
    template_name = "blog/post_list.html"
    context_object_name = "post_list"
    model = Post


class PostCreateView(generic.CreateView):
    pass
