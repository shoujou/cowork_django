from django.contrib.auth.mixins import UserPassesTestMixin


class EachUserPassesTestMixin(UserPassesTestMixin):
    def test_func(self):
        pk = self.kwargs['pk']
        return self.request.user == self.model.objects.get(id=pk).user


class EachAuthorPassesTestMixin(UserPassesTestMixin):
    def test_func(self):
        req_author = self.request.user.author
        pk = self.kwargs['pk']
        return req_author == self.model.objects.get(id=pk).author