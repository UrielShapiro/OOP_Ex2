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

    # factory#
    def sign_up(self, name, password):
        for u in self.users:
            if u.name == name:
                raise RuntimeError('name is not valid')
        if 4 < len(password) < 8:
            newUser = User.User(name, password, True)
            self.users.append(newUser)
            return newUser

    def log_in(self, name, password):
        for u in self.users:
            if u.name == name and u.password == password:
                u.logIn()

    def log_out(self, name):
        for u in self.users:
            if u.name == name:
                u.logOut()
