from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#We are going to create a new view to display a template when a user logs in.
@login_required
def user_dashboard(request):
    return render(request, 'main/dashboard.html')

#We are going to create a new view to display a template for reports.
@login_required
def reports(request):
    return render(request, 'main/reports.html')
