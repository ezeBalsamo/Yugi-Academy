from django import forms
from django.contrib.auth.models import User


class SendMessageForm(forms.Form):
    receiver = forms.ModelChoiceField(User.objects.all())
    content = forms.CharField(label='content', widget=forms.Textarea)


class MessageForm(forms.Form):
    receiver = forms.ModelChoiceField(User.objects.all())
