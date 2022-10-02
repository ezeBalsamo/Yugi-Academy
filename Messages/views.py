from datetime import datetime

from django.apps import apps
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from Messages.forms import SendMessageForm, MessageForm
from Messages.messages import Message
from assertions import InstanceCreationFailed, SystemRestrictionInfringed

message_system = apps.get_app_config('Messages').message_management_system


@login_required
def show_messages_to_user(request):
    sender = request.user
    if request.method == 'POST':
        form = MessageForm(request.POST, sender=sender)
        if form.is_valid():
            form_data = form.cleaned_data
            receiver = form_data.get('receiver')
            context = {
                'form': MessageForm(sender=sender),
                'conversation': message_system.conversation_between(sender, receiver)
            }
            return render(request, "messages.html", context)

    if request.method == 'GET':
        return render(request, "messages.html", {"form": MessageForm(sender=sender)})

    raise Exception(f'The {request.method} method was not expected')


@login_required
def send_message_to_user(request):
    sender = request.user
    if request.method == 'POST':
        form = SendMessageForm(request.POST, sender=sender)
        if form.is_valid():
            try:
                new_message = Message.from_form(sender, datetime.now(), form.cleaned_data)
                message_system.send_new_message(new_message)
                return render(request, "send_message.html", {"form": SendMessageForm(sender=sender)})
            except (InstanceCreationFailed, SystemRestrictionInfringed) as error:
                messages.error(request, str(error))
                return render(request, "send_message.html", {"form": SendMessageForm(sender=sender)})

    if request.method == 'GET':
        return render(request, "send_message.html", {"form": SendMessageForm(sender=sender)})

    raise Exception(f'The {request.method} method was not expected')
