from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from mytask.employee.models import Employees
from django.contrib.auth import get_user_model
User = get_user_model()
from django.core.exceptions import ValidationError
from django.forms import ModelForm #We import the ModelForm class, which will do all the heavy lifting for us.
from mytask.setup.models import ( 
     Gender, 
     Title,
     Position
)

class AddEmployeeForm(UserCreationForm):#As the base we used the built-in UserCreationForm, which defines the username and password fields. We extend this to include username, email and password.
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    # Here we add the extra form fields that we will use to create another model object when the new user is created (Employee model)
    employee_phone = forms.CharField(required=False)
    gender  = forms.ModelChoiceField(queryset=Gender.objects.filter(is_active='True'), required=True) #filter by active status of the gender
    
    class Meta(UserCreationForm.Meta): 
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]
        #remove the help texts on the username field
        help_texts = {
            'username': None,
            
        }
    #avoid duplicate emails
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError('Another user with that email already exists')
        return email

    '''
    Note that the save method is decorated with the transaction.atomic, 
    to make sure those three operations are done in a single database transaction and avoid data 
    inconsistencies in case of error.
    '''
    @transaction.atomic
    def save(self, commit=True):
        # Pop the fields out of self.cleaned_data
        employee_phone = self.cleaned_data.pop('employee_phone', None)
        gender = self.cleaned_data.pop('gender', None)
        user = super(AddEmployeeForm, self).save(commit=False) #commit = false so not to save before checking user roles and is_active.
        #Inside the save method, I’m setting the is_true = true, so that the created user is given Parent role by defaut.
        user.is_employee = True
        user.is_active = True #is_active will make the user to be active and able to login the system
        user.save() #save user in the database
        #We create an Parent profile to store the extra information, that is not available in the default user model.
        #now that we have successfully saved the user we can now use the user object just created to create a ParentProfile object with the extra form fields captured by the form
        Employees.objects.create(user=user, employee_phone=employee_phone, gender=gender)
        return user

class EmployeeUpdateForm(ModelForm): #UserUpdateForm class inherits from ModelForm.
        user = forms.CharField(required=False, disabled=True)
        title = forms.ModelChoiceField(queryset=Title.objects.filter(is_active='True'), disabled=True, required=True)
        employee_phone = forms.CharField(required=False, disabled=False)
        position = forms.ModelChoiceField(queryset=Position.objects.filter(is_active='True'), required=False, disabled=True)
        gender = forms.ModelChoiceField(queryset=Gender.objects.filter(is_active='True'), disabled=True, required=False) #filter by active status of the gender
        date_of_birth = forms.DateField(required=False, disabled=True)
        address = forms.CharField(required=True, disabled=False, widget=forms.Textarea(attrs={'rows': 2, 'cols': 6}))
        employee_profile_summary = forms.CharField(required=True, disabled=False, widget=forms.Textarea(attrs={'rows': 2, 'cols': 6}))
    
        class Meta: #The ModelForm class has an internal Meta class which we use to pass in the metadata options the ModelForm class needs to render our form:
            model = Employees
            fields = ['user', 'title', 'employee_phone', 'position', 'gender', 'date_of_birth', 'address', 'employee_profile_summary']

            help_texts = {
            'username': None,
             }