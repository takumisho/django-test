from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = "shoi"
        return context
    


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["num_services"] = "100000"
        context["skills"] = [
            "Python",
            "C++",
            "アルゴリズム"
        ]
        return context
        