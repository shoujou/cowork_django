from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth import get_user_model


class Author(models.Model):
    name = models.CharField(_("name"), max_length=150)
    user = models.OneToOneField(to=get_user_model(), 
                                verbose_name=_("user"), 
                                on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    title = models.CharField(_("title"), max_length=150)
    body = models.TextField(_("body"))
    created_date = models.DateTimeField(_("created date"), default=timezone.now)
    author = models.ForeignKey(to=Author,
                               verbose_name=_("author"), 
                               on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

