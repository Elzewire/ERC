from django.urls import path

from main import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('clients/', views.ClientView.as_view(), name='clients'),
    path('integration/', views.IntegrationView.as_view(), name='integration'),
    path('mobile/', views.MobileView.as_view(), name='mobile'),
    path('places/', views.PlacesView.as_view(), name='places'),
    path('services/', views.ServicesView.as_view(), name='services'),
]