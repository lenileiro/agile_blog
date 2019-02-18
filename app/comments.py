class Comment:
    def __init__(self):
        # Comment Parameters
        self.messages = []

    def set_message(self, message, author):
        pass

    def replied_to(self):
        pass

    def to_string(self):
        pass

    def delete_comment(self, message_id):
        """Deletes comment from list"""
        # Check instance of message id is int and list is not empty
        if isinstance(message_id, int) and len(self.messages) > 0:
            for message in self.messages:
                # Check ids match
                if message['id'] == message_id:
                    self.messages.remove(message)
                    return 'Comment Deleted'
                return 'Comment Doesnt Exist'
        return 'Invalid Id'
