from django.forms import Form, ModelForm

from .models import Author


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        exclude = ("user",)


