from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path('', views.AuthorListView.as_view(), name='author-list'),
    path('post/', views.PostListView.as_view(), name='post-list'),
]