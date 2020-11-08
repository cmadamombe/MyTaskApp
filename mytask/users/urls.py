from django.contrib.auth import views as auth_views
from mytask.users import views
from django.urls import include, path
from mytask.users import views

app_name = "users"
urlpatterns = [
    path('user/view', views.UserUpdateView.as_view(), name='user_update'),
    path('search/all/users', views.search_all_users, name='search_all_users'),
    path('search/active/users', views.search_all_users, name='search_active_users'),
    path('search/inactive/users', views.search_all_users, name='search_inactive_users'),
]


