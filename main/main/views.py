from typing import Any

from django.views.generic import TemplateView


# Create your views here.
class Homepage(TemplateView):
    """Homepage view for site"""

    http_method_names = ["get"]
    template_name = "main/home.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Home"
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
