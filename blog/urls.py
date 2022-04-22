from django.urls import path

from . import views

urlpatterns = [
    path('', views.AuthorListView.as_view(), name='author-list'),
    path('post/', views.PostListView.as_view(), name='post-list'),
]