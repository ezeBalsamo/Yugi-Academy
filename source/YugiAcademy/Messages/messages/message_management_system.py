from Messages.messages import Message


class MessageManagementSystem:

    def __init__(self):
        self.messages_repository = Message.objects

    def send_new_message(self, message):
        message.save()
