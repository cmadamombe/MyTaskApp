from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import forms as frms
User = get_user_model()
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm #We import the ModelForm class, which will do all the heavy lifting for us.
from allauth.account.forms import SignupForm

class UserChangeForm(frms.UserChangeForm):
    class Meta(frms.UserChangeForm.Meta):
        model = User

class UserCreationForm(frms.UserCreationForm):

    error_message = frms.UserCreationForm.error_messages.update(
        {"duplicate_username": _("This username has already been taken.")}
    )

    class Meta(frms.UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise ValidationError(self.error_messages["duplicate_username"])

class UserUpdateForm(ModelForm): #UserUpdateForm class inherits from ModelForm.
        username = forms.CharField(required=False, disabled=True)
        email = forms.EmailField(required=False, disabled=True)
        first_name = forms.CharField(required=False, disabled=True)
        middle_name = forms.CharField(required=False, disabled=True)
        last_name = forms.CharField(required=False, disabled=True)
        is_superuser = forms.BooleanField(required=False, disabled=True)
        is_staff = forms.BooleanField(required=False, disabled=True)
        is_active = forms.BooleanField(required=False, disabled=True)
        is_employee = forms.BooleanField(required=False, disabled=True)
        is_admin = forms.BooleanField(required=False, disabled=True)
        date_joined = forms.CharField(required=False, disabled=True)

        class Meta: #The ModelForm class has an internal Meta class which we use to pass in the metadata options the ModelForm class needs to render our form:
            model = User
            fields = ['username', 'email', 'first_name', 'middle_name', 'last_name', 'is_superuser', 'is_staff', 'is_active', 'is_employee',
            'is_admin', 'date_joined']

            help_texts = {
            'username': None,
            'is_superuser': None,
             }
