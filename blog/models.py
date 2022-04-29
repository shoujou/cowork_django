from django.db import models
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import uuid


class Author(models.Model):
    name = models.CharField(_("name"), max_length=150)
    dob = models.DateField(_("date of birth"), auto_now=False, auto_now_add=False, blank=True)
    profile = models.TextField(_("profile"))
    user = models.OneToOneField(to=get_user_model(), verbose_name=_("user"), on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class PostModelQuerySet(models.QuerySet):
    def search(self, key_string):
        query_set = self
        if key_string is not None:
            lookup_param = (
                Q(author__name__icontains=key_string)
              | Q(title__icontains=key_string) 
              | Q(body__icontains=key_string)
            )
            query_set = query_set.filter(lookup_param).distinct()
        return query_set


class PostManager(models.Manager):
    def get_queryset(self):
        return PostModelQuerySet(self.model, using=self._db)

    def search(self, key_string):
        return self.get_queryset().search(key_string)


class Post(models.Model):
    id = models.UUIDField(_("id"), primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(_("title"), max_length=150)
    body = models.TextField(_("body"))
    created_date = models.DateTimeField(_("created date"), 
                                        auto_now=False, auto_now_add=False,
                                        default=timezone.now)

    updated_date = models.DateTimeField(_("updated date"), 
                                        auto_now=False, auto_now_add=False,
                                        blank=True, null=True)
    author = models.ForeignKey(to=Author, verbose_name=_("author"), on_delete=models.CASCADE)
    objects = PostManager()

    class Meta:
        ordering = ["-updated_date", "-created_date"]

    def __str__(self) -> str:
        return "<Post:title=%s, author=%s>" % (self.title, self.author)

    def setnow_updated_date(self):
        self.updated_date = timezone.now()