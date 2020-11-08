from django.db import models
#from django.contrib.auth.models import User
from django.conf import settings
User = settings.AUTH_USER_MODEL
from mytask.setup.models import ( 
     Gender,  
     Title,
     Position
)
# Create your models here.
class Employees(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Title')    
    employee_phone = models.CharField(max_length=12, blank=True, null=True, verbose_name='Employee Phone')
    position = models.ForeignKey(Position, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Position')
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Gender')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Date of Birth')
    address = models.TextField(blank=True, null=True, verbose_name='Physical Address')
    employee_profile_summary = models.TextField(blank=True, null=True, verbose_name='Employee Profile Summary')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, editable=False, related_name='created_by', verbose_name='Created By')
    created_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Date Created')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, editable=False, related_name='modified_by', verbose_name='Modified By')
    modified_date = models.DateTimeField(auto_now=True, editable=False, verbose_name='Date Modified')
    is_active = models.BooleanField(default=True)

    class Meta:
        """Meta definition for Employee."""
        verbose_name = "Employee Profile"
        verbose_name_plural = 'Employees Profile'
        ordering = ('user',)
        
    def __str__(self):
        return '{}'.format(self.user)
