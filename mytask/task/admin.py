from django.contrib import admin
from mytask.task.models import Task

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Task Details:', {  # The first fieldset is named “Employee personal details”
            'description': "Please capture the task details: ",  # The first option sets the description for the group
            #'classes': ('collapse',), #Adds the collapse class to the fieldset. This will apply a JavaScipt accordion style that will make the fieldset appear collapsed when the form first displays
            'fields': (("task_reference","title","description"), ("assigned_to", "priority", "task_owner"), ("expected_completion_date", "status"))
        }),
    )
    # Chooses the fields to display on the form
    #list_display = ["task_reference", "title", "description", "assigned_to", "priority", "task_owner", "date_task_created", "expected_completion_date", "status", "created_by", "created_date", "modified_by", "modified_date"]
    list_display = ["task_reference", "title", "task_owner", "assigned_to", "priority"]
    #The fields that will be used to search the database
    #search_fields = ["task_reference", "title","description", "task_owner"]
    search_fields = ["task_reference", "title", "description"]
    #Field the database according to the selected fields by default
    list_filter = ('assigned_to','priority', 'status')
    #The results are in ascending order. To display results in descending order, use (-field_name e.g -user)
    ordering = ('date_task_created',)
