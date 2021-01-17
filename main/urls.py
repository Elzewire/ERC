from django.urls import path

from main import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('clients/', views.ClientView.as_view(), name='clients'),
    path('integration/', views.IntegrationView.as_view(), name='integration'),
    path('mobile/', views.MobileView.as_view(), name='mobile'),
    path('places/', views.PlacesView.as_view(), name='places'),
    path('faq/', views.FaqView.as_view(), name='faq'),
    path('info/', views.InfoView.as_view(), name='info'),
    path('certificate/', views.CertificateView.as_view(), name='certificate'),
    path('ipu/', views.IpuView.as_view(), name='ipu'),
    path('about/', views.AboutView.as_view(), name='about'),
]