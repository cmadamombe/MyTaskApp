from django.contrib import admin
from mytask.setup.models import ( 
     Gender,  
     Title,
     Position,
     Task_Status
)
# Register your models here.
@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    fieldsets = (("Gender Details", {"fields": ("code", "description", "is_active",)}),)
    list_display = ["code", "description", "created_by", "created_date", "modified_by", "modified_date", "is_active"]
    #search_fields = ["name","username","email"]

@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    fieldsets = (("Title Details", {"fields": ("code", "description", "is_active",)}),)
    list_display = ["code", "description", "created_by", "created_date", "modified_by", "modified_date", "is_active"]

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    fieldsets = (("Position Details", {"fields": ("code", "description", "is_active",)}),)
    list_display = ["code", "description", "created_by", "created_date", "modified_by", "modified_date", "is_active"]

@admin.register(Task_Status)
class Task_StatusAdmin(admin.ModelAdmin):
    fieldsets = (("Task Status Details", {"fields": ("code", "description", "is_active",)}),)
    list_display = ["code", "description", "created_by", "created_date", "modified_by", "modified_date", "is_active"]
