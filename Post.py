
class Post:
    def __init__(self, owner):
        self.owner = owner

    ######################
    def like(self, user):
        self.owner.my_notifications.append(f"{user.name} liked your post")

    ##########################################
    def comment(self, user, txt):
        pass
