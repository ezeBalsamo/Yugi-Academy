from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat the password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        # Remove help messages
        help_texts = {help: "" for help in fields}


class UpdatePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='Current password', widget=forms.PasswordInput)
    new_password1 = forms.CharField(label='New password', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Repeat the new password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["old_password", "new_password1", "new_password2"]
        # Remove help messages
        help_texts = {help: "" for help in fields}
