from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('registration/', views.signup, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),

]
