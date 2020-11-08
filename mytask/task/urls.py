from django.contrib.auth import views as auth_views
from mytask.task import views
from django.urls import include, path

app_name = "task"

urlpatterns = [
    path('add/new/task', views.AddNewTaskView.as_view(), name='add_new_task'),
    path('search/all/tasks', views.search_all_tasks, name='search_all_tasks'),#tasks assigned to clients
    path('search/all/mytasks', views.search_all_my_tasks, name='search_all_my_tasks'),#tasks assigned to employees
    path('search/all/thetasks', views.search_all_the_tasks, name='search_all_the_tasks'),#all tasks
    path('search/all/tasks/in/progress', views.search_all_tasks_in_progress, name='search_all_tasks_in_progress'),#all tasks in progress
]