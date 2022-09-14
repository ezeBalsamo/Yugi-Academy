from django import forms


class UserForm(forms.Form):
    email = forms.EmailField(max_length=50, required=False)
    username = forms.CharField(max_length=50, required=False)
    password = forms.CharField(max_length=25, required=False)
    name = forms.CharField(max_length=50, required=False)
    description = forms.CharField(required=False)
    web_site = forms.CharField(max_length=50, required=False)
    image = forms.ImageField(required=False)


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    password = forms.CharField(max_length=25)


class LogInForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=25)
