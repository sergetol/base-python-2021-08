from django.views.generic import TemplateView


class IndexTemplateView(TemplateView):
    extra_context = {
        "active_page": "index",
    }
    template_name = "root/index.html"


class AboutTemplateView(TemplateView):
    extra_context = {
        "active_page": "about",
    }
    template_name = "root/about.html"
