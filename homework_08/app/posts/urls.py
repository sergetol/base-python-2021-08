from django.urls import path

from .views import PostListView, PostCreateView, PostUpdateView

app_name = "posts"

urlpatterns = [
    path("", PostListView.as_view(), name="list"),
    path("add/", PostCreateView.as_view(), name="add"),
    path("<int:pk>/", PostUpdateView.as_view(), name="details"),
]
