import User


class Observer:
    def __init__(self, owner: User):
        self.owner = owner

    def update_like(self, user):
        self.owner.my_notifications.append(f"{user.name} liked your post")
        print(f"notification to {self.owner.name} : {user.name} liked your post")

    def update_comment(self, user, information):
        self.owner.my_notifications.append(f"{user.name} commented on your post")
        print(f"notification to {self.owner.name} : {user.name} commented on your post: {information}\n")

    def published_post_notify(self, user):
        user.my_notifications.append(f"{self.owner} has a new post")
