from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Gender, Title, Position, Task_Status
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django import forms
from .filters import GenderFilter, TitleFilter, PositionFilter, Task_StatusFilter
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

class AddGenderView(LoginRequiredMixin, CreateView):
    model = Gender
    template_name = 'setup/add_gender.html'
    fields = ('code', 'description')
    success_url = reverse_lazy('add_gender')

    def get_success_url(self):
        return reverse("setup:add_gender")
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.add_message(self.request, messages.SUCCESS, ("The Gender Instance Has Been Successfully Created."))
        return super().form_valid(form)

class AddTitleView(LoginRequiredMixin, CreateView):
    model = Title
    template_name = 'setup/add_title.html'
    fields = ('code', 'description')
    success_url = reverse_lazy('add_title')

    def get_success_url(self):
        return reverse("setup:add_title")
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.add_message(self.request, messages.SUCCESS, ("The Title Instance Has Been Successfully Created."))
        return super().form_valid(form)

class AddPositionView(LoginRequiredMixin, CreateView):
    model = Position
    template_name = 'setup/add_position.html'
    fields = ('code', 'description')
    success_url = reverse_lazy('add_position')

    def get_success_url(self):
        return reverse("setup:add_position")
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.add_message(self.request, messages.SUCCESS, ("The Position Instance Has Been Successfully Created."))
        return super().form_valid(form)

class AddTaskStatusView(LoginRequiredMixin, CreateView):
    model = Task_Status
    template_name = 'setup/add_task_status.html'
    fields = ('code', 'description')
    success_url = reverse_lazy('add_task_status')

    def get_success_url(self):
        return reverse("setup:add_task_status")
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.add_message(self.request, messages.SUCCESS, ("The Task Status Instance Has Been Successfully Created."))
        return super().form_valid(form)

@login_required
def search_gender(request):
    gender_list = Gender.objects.all()
    gender_filter = GenderFilter(request.GET, queryset=gender_list)
    return render(request, 'setup/gender_list.html', {'filter': gender_filter})

@login_required
def search_task_status(request):
    task_status_list = Task_Status.objects.all()
    task_status_filter = Task_StatusFilter(request.GET, queryset=task_status_list)
    return render(request, 'setup/task_status_list.html', {'filter': task_status_filter})

@login_required
def search_title(request):
    title_list = Title.objects.all()
    title_filter = TitleFilter(request.GET, queryset=title_list)
    return render(request, 'setup/title_list.html', {'filter': title_filter})

@login_required
def search_position(request):
    position_list = Position.objects.all()
    position_filter = PositionFilter(request.GET, queryset=position_list)
    return render(request, 'setup/position_list.html', {'filter': position_filter})
