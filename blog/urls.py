from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path('', views.PostListView.as_view(), name='post-list'),
    path('detail/<uuid:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('create/', views.PostCreateView.as_view(), name='post-create'),
    path('update/<uuid:pk>', views.PostUpdateView.as_view(), name='post-update'),
    path('delete/<uuid:pk>', views.PostDeleteView.as_view(), name='post-delete'),
    path('author/', views.AuthorListView.as_view(), name='author-list'),
    path('author/create/', views.AuthorCreateView.as_view(), name="author-create"),
    # path('author-detail:<int:pk>'),
]