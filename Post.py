import User


class Post:
    def __init__(self, owner):
        self.owner = owner

    ######################
    def like(self, user):
        self.owner.like_notify(user)

    def comment(self, user, txt):
        self.owner.comment_notify(user, txt)
