from django.forms import EmailField, Form, ModelForm
from django.contrib.auth import get_user_model


from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["email", "password1", "password2"]
        field_classes = {"email": EmailField}

