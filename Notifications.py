import User


class Notifications:
    def __init__(self, owner: User):
        self.owner = owner

    def update_like(self, user):
        self.owner.my_notifications.append(f"{user.name} liked your post")
        # Add a notification to the post owner notifications list.
        print(f"notification to {self.owner.name}: {user.name} liked your post")

    def update_comment(self, user, information):
        self.owner.my_notifications.append(f"{user.name} commented on your post")
        # Add a notification to the post owner notifications list.
        print(f"notification to {self.owner.name}: {user.name} commented on your post: {information}")

    def published_post_notify(self, user):
        user.my_notifications.append(f"{self.owner.name} has a new post")
        # Add a notification to the user notifications list about the new post.
