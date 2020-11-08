#from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL

class Gender(models.Model):
    code = models.CharField(verbose_name='Code', max_length=500)
    description = models.CharField(verbose_name='Description', max_length=500)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, editable=False, related_name='gender_created_by', verbose_name='Created By')
    created_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Date Created')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, editable=False, related_name='gender_modified_by', verbose_name='Modified By')
    modified_date = models.DateTimeField(auto_now=True, editable=False, verbose_name='Date Modified')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Gender"
        verbose_name_plural = 'Genders'
        ordering = ('code',)

    def __str__(self):
        return "{}".format(self.code)

class Title(models.Model):
    code = models.CharField(verbose_name='Code', max_length=500)
    description = models.CharField(verbose_name='Description', max_length=500)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, editable=False, related_name='title_created_by', verbose_name='Created By')
    created_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Date Created')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, editable=False, related_name='title_modified_by', verbose_name='Modified By')
    modified_date = models.DateTimeField(auto_now=True, editable=False, verbose_name='Date Modified')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Title"
        verbose_name_plural = 'Titles'
        ordering = ('code',)

    def __str__(self):
        return "{}".format(self.code)

class Position(models.Model):
    code = models.CharField(verbose_name='Code', max_length=500)
    description = models.CharField(verbose_name='Description', max_length=500)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, editable=False, related_name='position_created_by', verbose_name='Created By')
    created_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Date Created')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, editable=False, related_name='position_modified_by', verbose_name='Modified By')
    modified_date = models.DateTimeField(auto_now=True, editable=False, verbose_name='Date Modified')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Position"
        verbose_name_plural = 'Positions'
        ordering = ('code',)

    def __str__(self):
        return "{}".format(self.code)

class Task_Status(models.Model):
    code = models.CharField(verbose_name='Code', max_length=500)
    description = models.CharField(verbose_name='Description', max_length=500)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, editable=False, related_name='task_status_created_by', verbose_name='Created By')
    created_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Date Created')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, editable=False, related_name='task_status_modified_by', verbose_name='Modified By')
    modified_date = models.DateTimeField(auto_now=True, editable=False, verbose_name='Date Modified')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Task Status"
        verbose_name_plural = 'Task Status'
        ordering = ('code',)

    def __str__(self):
        return "{}".format(self.code)
