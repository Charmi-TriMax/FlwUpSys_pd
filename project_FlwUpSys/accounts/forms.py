from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Staff
from .user_types import get_user_type_choices
from django.contrib.auth.forms import PasswordChangeForm

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ResetPasswordForm(forms.Form):
    old_password = forms.CharField(
        label='Old Password', widget=forms.PasswordInput)
    new_password = forms.CharField(
        label='New Password', widget=forms.PasswordInput)
    # class ResetPasswordForm(forms.Form):
    confirm_new_password = forms.CharField(
        label='Confirm New Password', widget=forms.PasswordInput)

#     user = forms.CharField()  # Update with the actual field name
#     old_password = forms.CharField(widget=forms.PasswordInput)
#     reset_password = forms.CharField(widget=forms.PasswordInput)
#     confirm_reset_password = forms.CharField(widget=forms.PasswordInput)

#     def clean(self):
#         cleaned_data = super().clean()
#         old_password = cleaned_data.get('old_password')
#         reset_password = cleaned_data.get('reset_password')
#         confirm_reset_password = cleaned_data.get('confirm_reset_password')

#         if old_password == reset_password:
#             raise forms.ValidationError("old_password and new password can't be the same.")

#         if reset_password != confirm_reset_password:
#             raise forms.ValidationError("Passwords do not match.")

#         return cleaned_data


class RegistrationForm(forms.Form):
    USER_TYPE_CHOICES = get_user_type_choices()

    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    code = forms.CharField()
    isActive = forms.BooleanField()
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, required=True)
    Designation = forms.CharField(required=False)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    mobile = forms.CharField()
    Phone = forms.CharField(required=False)
    ForceReset = forms.BooleanField()
    Other1 = forms.CharField(required=False)
    Other2 = forms.CharField(required=False)
    CrDtTm = forms.DateTimeField(required=False)
    CrBy = forms.CharField(required=False)
    CrFrom = forms.CharField(required=False)
    UpdDtTm = forms.DateTimeField(required=False)
    UpdBy = forms.CharField(required=False)
    UpdFrom = forms.CharField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        user_type = cleaned_data.get('user_type')

        if user_type == 'superuser' and not cleaned_data.get('is_superuser'):
            raise forms.ValidationError(
                "Superuser type requires is_superuser to be True.")

        if user_type == 'manager' and not cleaned_data.get('is_manager'):
            raise forms.ValidationError(
                "Manager type requires is_manager to be True.")

        if user_type == 'general' and not cleaned_data.get('is_general'):
            raise forms.ValidationError(
                "General type requires is_general to be True.")

    def clean_user_type(self):
        user_type = self.cleaned_data.get('user_type')
        if user_type == 'superuser':
            self.cleaned_data['is_superuser'] = True
            self.cleaned_data['is_manager'] = False
            self.cleaned_data['is_general'] = False
        elif user_type == 'manager':
            self.cleaned_data['is_superuser'] = False
            self.cleaned_data['is_manager'] = True
            self.cleaned_data['is_general'] = False
        elif user_type == 'general':
            self.cleaned_data['is_superuser'] = False
            self.cleaned_data['is_manager'] = False
            self.cleaned_data['is_general'] = True

        return user_type
