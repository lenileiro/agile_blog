import datetime

"""manage users"""


class User(object):
    def __init__(self, name):
        self.name = name
        self._online_status = False
        self._last_seen = None
        self._class_received = self.__class__.__name__

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def is_logged_in(self, is_logged_in):
        return is_logged_in

    def last_logged_in_at(self, _last_seen):
        self._last_seen = _last_seen

    def login(self, _online_status):
        if _online_status is False:
            self._online_status = True
        return _online_status


class Moderator(User):
    def __init__(self, name):
        super(Moderator, self).__init__(name)


class Admin(User):
    def __init__(self, name):
        super(Admin, self).__init__(name)
