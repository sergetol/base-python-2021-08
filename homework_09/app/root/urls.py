from django.urls import path

from .views import IndexTemplateView, AboutTemplateView

app_name = "root"

urlpatterns = [
    path("", IndexTemplateView.as_view(), name="index"),
    path("about/", AboutTemplateView.as_view(), name="about"),
]
