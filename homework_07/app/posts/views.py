from django.shortcuts import render

from . import models


def list_posts(request):
    posts = models.Post.objects.all()
    context = {
        "active_page": "posts",
        "posts": posts,
    }
    return render(request, "posts/list.html", context)
