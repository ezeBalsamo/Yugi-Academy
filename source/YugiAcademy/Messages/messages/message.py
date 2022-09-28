from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

from assertions import enforce_not_blank, InstanceCreationFailed


def deleted_user():
    return get_user_model().objects.get_or_create(username='deleted_user')[0]


def enforce_are_different_users(user, another_user):
    if user.get_username() == another_user.get_username():
        raise InstanceCreationFailed("Sender and receiver must be different users.")


class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sender', on_delete=models.SET(deleted_user))
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='receiver', on_delete=models.SET(deleted_user))

    date_and_time_sent = models.DateTimeField()
    content = models.TextField()

    @classmethod
    def from_form(cls, user, date_and_time_sent, form_data):
        receiver = form_data.get('receiver')
        content = form_data.get('content')

        enforce_are_different_users(user, receiver)
        enforce_not_blank(content, "Content")

        return cls(sender=user, receiver=receiver, date_and_time_sent=date_and_time_sent, content=content)

    def __str__(self):
        return f'Message from {self.sender_username()} to {self.receiver_username()} at ' \
               f'{self.formatted_date_and_time_sent()}'

    def sender_username(self):
        return self.sender.get_username()

    def receiver_username(self):
        return self.receiver.get_username()

    def formatted_date_and_time_sent(self):
        return self.date_and_time_sent.strftime("%d/%m/%Y %H:%M:%S")




