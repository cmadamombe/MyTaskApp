from django import forms
from mytask.task.models import Task
import django_filters

class TaskFilter(django_filters.FilterSet):
    task_reference = django_filters.CharFilter(lookup_expr='icontains')
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    assigned_to = django_filters.CharFilter(lookup_expr='icontains')
    task_owner = django_filters.CharFilter(lookup_expr='icontains')
    #year_joined = django_filters.NumberFilter(name='date_joined', lookup_expr='year')
    #groups = django_filters.ModelMultipleChoiceFilter(queryset=Group.objects.all(),
        #widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Task
        fields = ['task_reference', 'title', 'description', 'assigned_to', 'task_owner']
