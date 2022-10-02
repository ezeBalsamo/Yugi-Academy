from django.apps import AppConfig


class MessagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Messages'
    message_management_system = None

    def ready(self):
        from .messages import MessageManagementSystem
        self.message_management_system = MessageManagementSystem()
