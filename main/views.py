from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class ClientView(TemplateView):
    template_name = 'cli.html'


class IntegrationView(TemplateView):
    template_name = 'int.html'


class MobileView(TemplateView):
    template_name = 'mob.html'


class PlacesView(TemplateView):
    template_name = 'places.html'


class InfoView(TemplateView):
    template_name = 'info.html'


class CertificateView(TemplateView):
    template_name = 'certificate.html'


class FaqView(TemplateView):
    template_name = 'faq.html'


class IpuView(TemplateView):
    template_name = 'ipu.html'


class AboutView(TemplateView):
    template_name = 'about.html'
