"""manage users"""
class User():
    def __init__(self, name):
        self.name = name
        self._online_status = False
        self._last_seen = None
        self._class_received = self.__class__.__name__

   
class moderator(User):
  def __init__(self, name):
    super().__init__(name)

class admin(User):
  def __init__(self, name):
    super().__init__(name)