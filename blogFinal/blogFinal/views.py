from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'index.html'

class NosotrosView(TemplateView):
    template_name = 'general/nosotros.html'