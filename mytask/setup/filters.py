from django import forms
from mytask.setup.models import ( 
     Gender,  
     Title,
     Position,
     Task_Status
) 
import django_filters

class GenderFilter(django_filters.FilterSet):
    code = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    #year_joined = django_filters.NumberFilter(name='date_joined', lookup_expr='year')
    #groups = django_filters.ModelMultipleChoiceFilter(queryset=Group.objects.all(),
        #widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Gender
        fields = ['code', 'description']

class Task_StatusFilter(django_filters.FilterSet):
    code = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    #year_joined = django_filters.NumberFilter(name='date_joined', lookup_expr='year')
    #groups = django_filters.ModelMultipleChoiceFilter(queryset=Group.objects.all(),
        #widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Task_Status
        fields = ['code', 'description']

class TitleFilter(django_filters.FilterSet):
    code = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    #year_joined = django_filters.NumberFilter(name='date_joined', lookup_expr='year')
    #groups = django_filters.ModelMultipleChoiceFilter(queryset=Group.objects.all(),
        #widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Title
        fields = ['code', 'description']

class PositionFilter(django_filters.FilterSet):
    code = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    #year_joined = django_filters.NumberFilter(name='date_joined', lookup_expr='year')
    #groups = django_filters.ModelMultipleChoiceFilter(queryset=Group.objects.all(),
        #widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Position
        fields = ['code', 'description']