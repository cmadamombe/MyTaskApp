from django import forms
from mytask.clients.models import Clients
import django_filters

class ClientFilter(django_filters.FilterSet):
    user = django_filters.CharFilter(lookup_expr='icontains')
    client_phone = django_filters.CharFilter(lookup_expr='icontains')
    #year_joined = django_filters.NumberFilter(name='date_joined', lookup_expr='year')
    #groups = django_filters.ModelMultipleChoiceFilter(queryset=Group.objects.all(),
        #widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Clients
        fields = ['user', 'client_phone']