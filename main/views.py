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


class ServicesView(TemplateView):
    template_name = 'services.html'
