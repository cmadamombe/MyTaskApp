from django import forms
from mytask.employee.models import Employees
import django_filters

class EmployeeFilter(django_filters.FilterSet):
    user = django_filters.CharFilter(lookup_expr='icontains')
    employee_phone = django_filters.CharFilter(lookup_expr='icontains')
    #year_joined = django_filters.NumberFilter(name='date_joined', lookup_expr='year')
    #groups = django_filters.ModelMultipleChoiceFilter(queryset=Group.objects.all(),
        #widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Employees
        fields = ['user', 'employee_phone']