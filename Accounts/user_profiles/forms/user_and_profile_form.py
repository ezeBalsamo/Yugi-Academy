from django import forms
from django.contrib.auth.forms import UsernameField


class UserAndProfileForm(forms.Form):
    username = UsernameField(disabled=True, label_suffix='', required=False)
    avatar = forms.ImageField(label_suffix='', required=False)
    first_name = forms.CharField(label='First name', label_suffix='',  widget=forms.TextInput, required=False)
    last_name = forms.CharField(label='Last name', label_suffix='', widget=forms.TextInput, required=False)
    email = forms.EmailField(label_suffix='', required=False)
    description = forms.CharField(label='Description', label_suffix='', widget=forms.Textarea, required=False)
    social_network_link = forms.URLField(label='Link to social network', label_suffix='', required=False)
