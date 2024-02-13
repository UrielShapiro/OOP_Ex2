import User


class Post:
    def __init__(self, owner):
        self.owner = owner

    def like(self, user: 'User'):
        self.owner.like_notify(user)    # If a user likes a post, the post owner will be notified.

    def comment(self, user: User, txt: str):
        self.owner.comment_notify(user, txt)    # If a user comments on a post, the post owner will be notified.
