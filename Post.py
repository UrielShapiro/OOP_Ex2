import User


class Post:
    def __init__(self, owner):
        self.owner = owner

    def like(self, user: 'User'):
        self.owner.like_notify(user)

    def comment(self, user: User, txt: str):
        self.owner.comment_notify(user, txt)
