from datetime import datetime
from comments import Comment

"""manage users"""
class User():
    def __init__(self, name):
        self.name = name
        self._online_status = False
        self._last_seen = None
        self._lobby = Comment()
        self._class_received = self.__class__.__name__

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def is_logged_in(self):
        return self.is_logged_in

    def last_logged_in_at(self):
        self._last_seen = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def login(self, _online_status):
        self._online_status = True
        
    def log_out(self):
        self._online_status = False
        self.last_logged_in_at()
  
  
class moderator(User):
  def __init__(self, name):
    super().__init__(name)

class admin(User):
  def __init__(self, name):
    super().__init__(name)