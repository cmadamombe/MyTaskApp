from django.contrib.auth import views as auth_views
from mytask.clients import views
from django.urls import include, path

app_name = "clients"

urlpatterns = [
    path('add/new/client', views.AddClientView.as_view(), name='add_new_client'),
    path('update/client/details', views.ClientUpdateView.as_view(), name='update_client_details'),
    path('search/all/active/clients', views.search_all_active_clients, name='search_all_active_clients'),
    path('search/all/inactive/clients', views.search_all_inactive_clients, name='search_all_inactive_clients'),
]