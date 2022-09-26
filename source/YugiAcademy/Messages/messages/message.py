from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models


def deleted_user():
    return get_user_model().objects.get_or_create(username='deleted_user')[0]


class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sender', on_delete=models.SET(deleted_user))
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='receiver', on_delete=models.SET(deleted_user))
    date_and_time_sent = models.DateTimeField()
    content = models.TextField()

    def __str__(self):
        return f'Message from {self.sender_username()} to {self.receiver_username()} at {self.date_and_time_sent}'

    def sender_username(self):
        return self.sender.get_username()

    def receiver_username(self):
        return self.receiver.get_username()



