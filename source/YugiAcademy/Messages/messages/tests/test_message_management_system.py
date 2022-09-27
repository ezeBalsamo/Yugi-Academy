from datetime import datetime

import pytest
from django.contrib.auth.models import User

from Messages.messages import MessageManagementSystem, Message
from assertions import assert_is_empty, assert_the_only_one_in


def user(username, password):
    new_user = User(username=username, password=password)
    new_user.save()
    return new_user


def nico():
    return user(username='Nicoleta', password='Nicoleta12345')


def guido():
    return user(username='Guido', password='Guido12345')


def greetings_message():
    sender = guido()
    date_and_time_sent = datetime.now()
    form_data = {
        'receiver': nico(),
        'content': 'Hi, Nico!'
    }
    return Message.from_form(user=sender, date_and_time_sent=date_and_time_sent, form_data=form_data)


@pytest.mark.django_db
class TestMessageManagementSystem:

    @pytest.fixture(autouse=True)
    def set_up(self):
        self.system = MessageManagementSystem()

    def test_store_message(self):
        assert_is_empty(self.system.messages())
        message = greetings_message()
        self.system.send_new_message(message)
        assert_the_only_one_in(self.system.messages(), message)
