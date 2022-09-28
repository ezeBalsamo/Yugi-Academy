from django.urls import path

from .views import show_messages_to_user, send_message_to_user

urlpatterns = [
    path('', show_messages_to_user, name="messages"),
    path('send_message', send_message_to_user, name="send_message"),
]
