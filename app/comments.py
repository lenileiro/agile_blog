import datetime

class Comment():
    def __init__(self):
        self.messages = []

    def get_author(self):
        pass
        
    def set_message(self, message,author):
        self.messages = self.messages.append({
            "author": author,
            "message": message,
            "timestamp": datetime.datetime.now(),
            "id": len(self.messages)
        })

    def edit_message(self, id, newmessage):
        for message in self.messages:
            if message["id"] == id:
                message["message"] = newmessage



    def created_at(self):
        pass
    def replied_to(self):
        pass

    def to_string(self):
        pass

    