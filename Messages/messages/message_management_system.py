from Messages.messages import Message


class MessageManagementSystem:

    def __init__(self):
        self.messages_repository = Message.objects

    def messages(self):
        return list(self.messages_repository.all())

    def send_new_message(self, message):
        message.save()

    def messages_from(self, sender, to):
        return self.messages_repository.filter(sender=sender).filter(receiver=to)

    def conversation_between(self, user, another_user):
        messages_sent_by_user = self.messages_from(user, to=another_user)
        messages_received_by_user = self.messages_from(another_user, to=user)
        messages = messages_sent_by_user | messages_received_by_user
        return messages.order_by('date_and_time_sent')
