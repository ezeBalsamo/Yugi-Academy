from datetime import datetime

from django.apps import apps
from django.shortcuts import render

from Messages.forms import SendMessageForm, MessageForm
from Messages.messages import Message

message_system = apps.get_app_config('Messages').message_management_system


def show_messages_to_user(request):
    user = request.user
    if request.method == 'POST':
        form = MessageForm(request.POST, request)
        if form.is_valid():
            form_data = form.cleaned_data
            receiver = form_data.get('receiver')
            context = {
                'conversation': message_system.conversation_between(user, receiver)
            }
            return render(request, "conversation.html", context)

    if request.method == 'GET':
        return render(request, "messages.html", {"form": MessageForm()})


def send_message_to_user(request):
    user = request.user
    if request.method == 'POST':
        form = SendMessageForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            date_and_time_sent = datetime.now()
            new_message = Message.from_form(user, date_and_time_sent, form_data)
            message_system.send_new_message(new_message)

    return render(request, "send_message.html", {"form": SendMessageForm()})

