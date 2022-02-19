from django.views.generic import ListView, CreateView, UpdateView

from .models import Post


class PostMixin:
    extra_context = {
        "active_page": "posts",
    }
    model = Post


class PostListView(PostMixin, ListView):
    template_name = "posts/list.html"
    context_object_name = "posts"


class PostCreateView(PostMixin, CreateView):
    template_name = "posts/add_or_update.html"
    fields = ["title", "body"]


class PostUpdateView(PostMixin, UpdateView):
    template_name = "posts/add_or_update.html"
    fields = ["title", "body"]
