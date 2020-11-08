from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
from mytask.clients.models import Clients
from mytask.employee.models import Employees
from mytask.setup.models import Task_Status
# Create your models here.
PRIORITY = (
    ('Normal Process', "Normal Process"),
    ('Fast Process', "Fast Process")
)
class Task(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    task_reference = models.CharField(max_length=100, blank=True, null=True, verbose_name='Reference') #This is set manually nd should be the same as the invoice number.
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name='Title')
    description = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Description')
    assigned_to = models.ForeignKey(Employees, on_delete=models.CASCADE, blank=True, null=True, editable=True, related_name='task_assigned_to', verbose_name='Assigned To')
    priority = models.CharField(
        max_length=100,
        choices=PRIORITY,
        default='Normal Process',
        help_text="Task Priority Status"
    )
    task_owner = models.ForeignKey(Clients, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Task Owner')
    date_task_created = models.DateField(auto_now_add=True, editable=False, verbose_name='Date Created')
    expected_completion_date = models.DateField(verbose_name='Expected Completion Date')
    status = models.ForeignKey(Task_Status, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Status')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, editable=False, related_name='task_created_by', verbose_name='Created By')
    created_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Date Created')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, editable=False, related_name='task_modified_by', verbose_name='Modified By')
    modified_date = models.DateTimeField(auto_now=True, editable=False, verbose_name='Date Modified')

    class Meta:
        """Meta definition for Task."""
        verbose_name = "Task Profile"
        verbose_name_plural = 'Tasks Profile'
        ordering = ('created_date',)

    def __str__(self):
        return '{}'.format(self.title)

