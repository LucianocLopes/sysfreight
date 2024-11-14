from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class PageTitleViewMixin:
    title = ""

    def get_title(self):
        """
        Return the class title attr by default,
        but you can override this method to further customize
        """
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.get_title()
        return context

class IndexView(LoginRequiredMixin, PageTitleViewMixin, TemplateView):
    template_name = "core/index.html"
    title = "HEMAFRAN ADM"
