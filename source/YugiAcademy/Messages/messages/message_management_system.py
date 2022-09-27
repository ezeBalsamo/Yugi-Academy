from Messages.messages import Message


class MessageManagementSystem:

    def __init__(self):
        self.messages_repository = Message.objects

    def messages(self):
        return list(self.messages_repository.all())

    def send_message(self, message):
        message.save()
