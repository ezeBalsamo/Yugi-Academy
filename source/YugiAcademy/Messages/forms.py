from django import forms
from django.contrib.auth.models import User


class MessageForm(forms.Form):
    def __init__(self, *args, **kwargs):
        sender = kwargs.pop('sender')
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['receiver'].queryset = User.objects.exclude(username=sender.get_username())

    receiver = forms.ModelChoiceField(queryset=User.objects.none())


class SendMessageForm(MessageForm):
    content = forms.CharField(label='Content', widget=forms.Textarea)
