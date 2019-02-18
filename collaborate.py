class Comment():
    def __init__(self):
        self.comments = []
    
    def createComment(self, message, author):
        pass

    def deleteComment(self, id):
        pass
    

class User():
    def __init__(self, username):
        self.username = username
        self.lastLoggedInAt = None


    def editComment(self, username):
        pass


class Moderator(User):
    def deleteAnyComment(self):
        pass


class Admin(Moderator):
    def editComment(self):
        pass
