from django import forms


class UserForm(forms.Form):
    email = forms.EmailField(max_length=50)
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=25)
    name = forms.CharField(max_length=50)
    field_description = forms.DateField()
    web_site = forms.CharField(max_length=50)
    image = forms.ImageField()


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    password = forms.CharField(max_length=25)


class LogInForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=25)
