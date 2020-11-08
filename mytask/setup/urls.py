from django.contrib.auth import views as auth_views
from mytask.setup import views
from django.urls import include, path

app_name = "setup"

urlpatterns = [
    path('add/gender', views.AddGenderView.as_view(), name='add_gender'),
    path('add/title', views.AddTitleView.as_view(), name='add_title'),
    path('add/position', views.AddPositionView.as_view(), name='add_position'),
    path('add/task/status', views.AddTaskStatusView.as_view(), name='add_task_status'),
    path('search/gender', views.search_gender, name='search_gender'),
    path('search/title', views.search_title, name='search_title'),
    path('search/position', views.search_position, name='search_position'),
    path('search/task/status', views.search_task_status, name='search_task_status'),
]