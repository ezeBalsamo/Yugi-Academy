from django import forms
from django.contrib.auth.forms import UsernameField


class UserAndProfileForm(forms.Form):
    username = UsernameField(disabled=True, required=False)
    avatar = forms.ImageField(required=False)
    first_name = forms.CharField(label='First name', widget=forms.TextInput, required=False)
    last_name = forms.CharField(label='Last name', widget=forms.TextInput, required=False)
    email = forms.EmailField(required=False)
    description = forms.CharField(label='Description', widget=forms.Textarea, required=False)
    social_network_link = forms.URLField(label='Link to social network', required=False)
