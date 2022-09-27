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
            messages_sent = Message.objects.filter(sender=user).filter(receiver=form_data.get('receiver'))
            messages_received = Message.objects.filter(sender=form_data.get('receiver')).filter(receiver=user)
            messages_between_user_and_receiver = messages_sent | messages_received
            ordered_messages_between_user_and_receiver = messages_between_user_and_receiver. \
                order_by('date_and_time_sent')
            context = {
                'conversation': ordered_messages_between_user_and_receiver
            }
            return render(request, "conversation.html", context)

    if request.method == 'GET':
        return render(request, "messages.html", {"form": MessageForm()})


def send_message_to_user(request):
    user = request.user
    if request.method == 'POST':
        form = SendMessageForm(request.POST, request)
        if form.is_valid():
            form_data = form.cleaned_data
            date_and_time_sent = datetime.now()
            new_message = Message.from_form(user, date_and_time_sent, form_data)
            message_system.send_message(new_message)

    return render(request, "send_message.html", {"form": SendMessageForm()})

