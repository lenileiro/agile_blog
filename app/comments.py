import datetime


class Comment:
    def __init__(self):
        # Comment Parameters
        self.messages = []

    def get_author(self):
        pass

    def set_message(self, message, author):
        """Sets message"""
        self.messages.append({
            "author": author,
            "message": message,
            "timestamp": datetime.datetime.now(),
            "id": len(self.messages)
        })

    def get_list(self):
        return self.messages

    def edit_message(self, id, newmessage):
        """Edits message"""
        for message in self.messages:
            if message["id"] == id:
                message["message"] = newmessage

    def replied_to(self):
        pass

    def to_string(self):
        pass

    def delete_comment(self, message_id):
        """Deletes comment from list"""
        # Check instance of message id is int and list is not empty
        if isinstance(message_id, int):
            for message in self.messages:
                # Check ids match
                if message['id'] == message_id:
                    self.messages.remove(message)
                    return 'Comment Deleted'
                return 'Comment Doesnt Exist'
        return 'Invalid Id'
