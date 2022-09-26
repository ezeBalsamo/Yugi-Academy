from datetime import datetime

import pytest
from django.contrib.auth.models import User
from assertions import InstanceCreationFailed

from Messages.messages import Message


def test_content_message_must_not_be_blank():
    sender = User(username='Guido', password='Guido12345')
    receiver = User(username='Nicoleta', password='Nicoleta12345')
    form_data = {
        'receiver': receiver,
        'content': ''
    }
    date_and_time_sent = datetime.now()

    with pytest.raises(InstanceCreationFailed) as exception_info:
        Message.from_form(user=sender, date_and_time_sent=date_and_time_sent, form_data=form_data)
    assert exception_info.message_text() == 'Content must not be blank.'


def test_sender_and_receiver_must_be_different_users():
    sender = User(username='Guido', password='Guido12345')
    receiver = User(username='Guido', password='Guido12345')
    form_data = {
        'receiver': receiver,
        'content': 'Hola Guido, cómo estás?'
    }
    date_and_time_sent = datetime.now()

    with pytest.raises(InstanceCreationFailed) as exception_info:
        Message.from_form(user=sender, date_and_time_sent=date_and_time_sent, form_data=form_data)
    assert exception_info.message_text() == 'Sender and receiver must be different users.'


def test_instance_creation_and_accessing():
    sender = User(username='Guido', password='Guido12345')
    receiver = User(username='Nicoleta', password='Nicoleta12345')
    form_data = {
        'receiver': receiver,
        'content': 'Hola Nico, cómo estás?'
    }
    date_and_time_sent = datetime.now()

    message = Message.from_form(user=sender, date_and_time_sent=date_and_time_sent, form_data=form_data)
    assert message.receiver.get_username() == 'Nicoleta'
    assert message.sender.get_username() == 'Guido'
    assert message.date_and_time_sent == date_and_time_sent.strftime("%d/%m/%Y %H:%M:%S")
    assert message.content == 'Hola Nico, cómo estás?'
