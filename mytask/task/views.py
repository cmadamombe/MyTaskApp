from django.contrib import messages
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from mytask.task.forms import AddNewTaskForm
from django.contrib.auth import get_user_model
User = get_user_model()
from django.urls import reverse
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from mytask.task.models import Task
from .filters import TaskFilter
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
class AddNewTaskView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = AddNewTaskForm
    template_name = 'task/add_new_task.html'
    success_url = reverse_lazy('add_new_task')

    def get_success_url(self):
        return reverse("task:add_new_task")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.add_message(self.request, messages.SUCCESS, ("New Task details have been successfully added!"))
        return super().form_valid(form)

#Function based view to search the tasks in the database assigned to task owner/clients
@login_required
def search_all_tasks(request):
    task_list = Task.objects.filter(task_owner=request.user.clients)
    task_filter = TaskFilter(request.GET, queryset=task_list)
    return render(request, 'task/all_task_list.html', {'filter': task_filter})

#Function based view to search the tasks in the database assigned to an employee/staff
@login_required
def search_all_my_tasks(request):
    mytask_list = Task.objects.filter(assigned_to=request.user.employees)
    mytask_filter = TaskFilter(request.GET, queryset=mytask_list)
    return render(request, 'task/all_task_list.html', {'filter': mytask_filter})

#Function based view to search the tasks in the database 
def search_all_the_tasks(request):
    thetask_list = Task.objects.all()
    thetask_filter = TaskFilter(request.GET, queryset=thetask_list)
    return render(request, 'task/all_task_list.html', {'filter': thetask_filter})

#Function based view to search the tasks in the database that are in progress
@login_required
def search_all_tasks_in_progress(request):
    tasks_in_progress_list = Task.objects.exclude(status__code='Closed')
    tasks_in_progress_list_filter = TaskFilter(request.GET, queryset=tasks_in_progress_list)
    return render(request, 'task/all_task_list.html', {'filter':  tasks_in_progress_list_filter})
