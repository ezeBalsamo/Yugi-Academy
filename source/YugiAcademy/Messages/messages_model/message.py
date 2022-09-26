from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models


def deleted_user():
    return get_user_model().objects.get_or_create(username='deleted_user')[0]


class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(deleted_user))
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(deleted_user))
    date_and_time_sent = models.DateTimeField()
    content = models.TextField()

    def __str__(self):
        return f'Rem: {self.remitent_user.get_username()} -> Dest: {self.destinatary_user.get_username()} - DateTime: {self.date_and_time}'
