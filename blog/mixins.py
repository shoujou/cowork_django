from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist


class UserMatchTestMixin(UserPassesTestMixin):
    def test_func(self):
        pk = self.kwargs['pk']
        return self.request.user == self.model.objects.get(id=pk).user


class AuthorMatchTestMixin(UserPassesTestMixin):
    def test_func(self):
        req_author = self.request.user.author
        pk = self.kwargs['pk']
        return req_author == self.model.objects.get(id=pk).author


class HasAuthorAccountTestMixin(UserPassesTestMixin):
    """
    if user already has author account, 
    user is redirected blog:post-list.
    """
    def test_func(self):
        return not self.model.objects.filter(user=self.request.user).exists()

    def dispatch(self, request, *args, **kwargs):
        user_test_result = self.get_test_func()()
        if not user_test_result:
            messages.warning(request, "You already have an author account.")
            return redirect("blog:post-list")
        return super().dispatch(request, *args, **kwargs)
