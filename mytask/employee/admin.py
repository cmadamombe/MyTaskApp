from django.contrib import admin
from mytask.employee.models import Employees

# Register your models here.
@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Employee Personal Details:', {  # The first fieldset is named “Employee personal details”
            'description': "Please capture the employees personal details: ",  # The first option sets the description for the group
            #'classes': ('collapse',), #Adds the collapse class to the fieldset. This will apply a JavaScipt accordion style that will make the fieldset appear collapsed when the form first displays
            'fields': (("user","title", "is_active"), ("date_of_birth", "employee_phone"), ("position", "gender"))
        }),

        ('Physical Address & Profile Summary:', {  # The second fieldset/group
            'description': "Please capture the employees address and profile: ",  # The  option sets the description for the group
            'classes': ('collapse',), #Adds the collapse class to the fieldset. This will apply a JavaScipt accordion style that will make the fieldset appear collapsed when the form first displays
            'fields': ("address", "employee_profile_summary")
        }),
    )  
    # Chooses the fields to display on the form
    list_display = ["user", "employee_phone", "date_of_birth", "gender", "created_by", "created_date", "modified_by", "modified_date", "is_active"]
    #The fields that will be used to search the database
    search_fields = ["user","employee_phone"]
    #Field the database according to the selected fields by default
    list_filter = ('gender', 'position')
    #The results are in ascending order. To display results in descending order, use (-field_name e.g -user)
    ordering = ('user',)
