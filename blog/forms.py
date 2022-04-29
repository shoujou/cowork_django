from django import forms

from .models import Author, Post


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        exclude = ("user",)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ("author",)


class PostSearchForm(forms.Form):
    string = forms.CharField(max_length=100,
                             help_text="",required=True)

