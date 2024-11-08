from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.population_list, name='population_list'),
    path('population/new/', views.population_create, name='population_create'),
    path('populations/<int:pk>/', views.population_detail, name='population_detail'),


    path('locations/', views.location_list, name='location_list'),
    path('locations/<int:pk>/', views.location_detail, name='location_detail'),
    path('locations/new/', views.location_create, name='location_create'),


]
