from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name = "main"
urlpatterns = [
    path('dashboard', views.user_dashboard, name='user_dashboard'),
    path('reports', views.reports, name='reports'),
]