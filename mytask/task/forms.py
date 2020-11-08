from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from mytask.employee.models import Employees
from mytask.clients.models import Clients
from mytask.task.models import Task
from django.contrib.auth import get_user_model
User = get_user_model()
from django.core.exceptions import ValidationError
from django.forms import ModelForm #We import the ModelForm class, which will do all the heavy lifting for us.
from mytask.setup.models import Task_Status

PRIORITY = (
    ('Normal Process', "Normal Process"),
    ('Fast Process', "Fast Process")
)
class AddNewTaskForm(ModelForm): #inherits from ModelForm.
        task_reference = forms.CharField(required=True, disabled=False)
        title = forms.CharField(required=True, disabled=False)
        description = forms.CharField(required=True, disabled=False)
        assigned_to = forms.ModelChoiceField(queryset=Employees.objects.all(), required=True, disabled=False)
        priority = forms.ChoiceField(choices=PRIORITY, required=True, disabled=False)
        task_owner = forms.ModelChoiceField(queryset=Clients.objects.filter(is_active='True'), required=True, disabled=False)
        expected_completion_date = forms.DateField(required=True, disabled=False)
        status = forms.ModelChoiceField(queryset=Task_Status.objects.filter(is_active='True'), required=True, disabled=False)
        class Meta: #The ModelForm class has an internal Meta class which we use to pass in the metadata options the ModelForm class needs to render our form:
            model = Task
            fields = ['task_reference', 'title', 'description', 'assigned_to', 'priority', 'task_owner', 'expected_completion_date', 'status']
            #help_texts = {
            #'username': None,
            #}
