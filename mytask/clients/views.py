from django.contrib import messages
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from mytask.clients.forms import AddClientForm, ClientUpdateForm
from django.contrib.auth import get_user_model
User = get_user_model()
from django.urls import reverse
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from .models import Clients
from django.shortcuts import render
from .filters import ClientFilter
from django.contrib.auth.decorators import login_required

# Create your views here.

class AddClientView(LoginRequiredMixin, CreateView):
    model = User
    form_class = AddClientForm
    template_name = 'clients/add_new_client.html'
    success_url = reverse_lazy('add_new_client')

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'client'
        return super().get_context_data(**kwargs)
    
    def get_success_url(self):
        return reverse("clients:add_new_client")

    def form_valid(self, form):
        #form.instance.created_by.set([User.objects.get(pk=request.user.pk)])
        messages.add_message(self.request, messages.SUCCESS, ("New client details have been successfully added!"))
        return super().form_valid(form)

class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Clients
    form_class = ClientUpdateForm
    template_name = 'clients/client_update_form.html'
    success_url = reverse_lazy('update_client_details')

    def get_success_url(self):
        return reverse("clients:update_client_details")#, kwargs={"username": self.request.user.username})

    def get_object(self):
        return Clients.objects.get(user=self.request.user)
       
    def form_valid(self, form):
        #form.instance.modified_by.set([self.request.user])
        messages.add_message(
            self.request, messages.INFO, _("The client information have been successfully updated")
        )
        return super().form_valid(form)

#Function based view to search active clients in the database
@login_required
def search_all_active_clients(request):
    active_client_list = Clients.objects.filter(is_active="True")
    active_client_filter = ClientFilter(request.GET, queryset=active_client_list)
    return render(request, 'clients/all_client_list.html', {'filter': active_client_filter})

#Function based view to search inactive clients in the database
@login_required
def search_all_inactive_clients(request):
    inactive_client_list = Clients.objects.filter(is_active="False")
    inactive_client_filter = ClientFilter(request.GET, queryset=inactive_client_list)
    return render(request, 'clients/all_client_list.html', {'filter': inactive_client_filter})