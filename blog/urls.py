from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path('', views.PostListView.as_view(), name='post-list'),
    path('author/', views.AuthorListView.as_view(), name='author-list'),
    path('author/create/', views.AuthorCreateView.as_view(), name="author-create"),
    # path('author-detail:<int:pk>'),
]