from django.views.generic import TemplateView
from services.models import Service 
from portfolio.models import Realisation 
from pages.models import Temoignage

class HomePageView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['services'] = Service.objects.filter(is_active=True).order_by('order')[:4]

        context['realisations'] = Realisation.objects.all().order_by('-realization_date')[:3]

        context['temoignages'] = Temoignage.objects.filter(is_published=True).order_by('-testimony_date')[:3]

        return context
