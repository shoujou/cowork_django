from django.forms import Form, ModelForm

from .models import Author, Post


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        exclude = ("user",)


class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ("author",)