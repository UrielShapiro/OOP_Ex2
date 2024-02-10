import User
import Post

_instance = None


def instance():
    return _instance


class SocialNetwork:
    users = []

    def __init__(self, name):
        if _instance is None:
            self.name = name
        else:
            raise RuntimeError('Call instance() instead')

    def sign_up(self, name, password):
        for u in self.users:
            if u.name == name:
                raise RuntimeError('name is not valid')
        if 4 < len(password) < 8:
            self.users.append(User.User(name, password, True))

    def log_in(self, name, password):
        for u in self.users:
            if u.name == name and u.password == password:
                u.logIn()

    def log_out(self, name):
        for u in self.users:
            if u.name == name:
                u.logOut()
