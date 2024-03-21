from django.views.generic import TemplateView


# Create your views here.
class Homepage(TemplateView):
    """Homepage view for site"""

    http_method_names = ["get"]
    template_name = "main/home.html"

    def get(self, *args, **kwargs):
        """Get method for Homepage view"""
        return super().get(self.request)
