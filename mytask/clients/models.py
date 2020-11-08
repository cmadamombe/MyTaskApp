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
class Clients(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Title')    
    client_phone = models.CharField(max_length=12, blank=True, null=True, verbose_name='Client Phone')
    position = models.ForeignKey(Position, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Position')
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Gender')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Date of Birth')
    address = models.TextField(blank=True, null=True, verbose_name='Physical Address')
    client_profile_summary = models.TextField(blank=True, null=True, verbose_name='Client Profile Summary')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, editable=False, related_name='client_created_by', verbose_name='Created By')
    created_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Date Created')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, editable=False, related_name='client_modified_by', verbose_name='Modified By')
    modified_date = models.DateTimeField(auto_now=True, editable=False, verbose_name='Date Modified')
    is_active = models.BooleanField(default=True)

    class Meta:
        """Meta definition for Client."""
        verbose_name = "Client Profile"
        verbose_name_plural = 'Clients Profile'
        ordering = ('user',)
        
    def __str__(self):
        return '{}'.format(self.user)

