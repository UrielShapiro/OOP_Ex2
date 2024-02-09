import User
import Post


class SocialNetwork:
    users = []
    posts = []

    def __init__(self, name):
        self.name = name

    def sign_up(self, name, password):
        if 4 < len(password) < 8:
            self.users.add(User(name, password))
