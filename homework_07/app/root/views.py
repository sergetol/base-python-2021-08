from django.shortcuts import render


def index(request):
    context = {
        "active_page": "index",
    }
    return render(request, "root/index.html", context)


def about(request):
    context = {
        "active_page": "about",
    }
    return render(request, "root/about.html", context)
