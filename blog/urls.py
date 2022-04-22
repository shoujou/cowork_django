from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.PostListView.as_view(), name="post-list"),
]