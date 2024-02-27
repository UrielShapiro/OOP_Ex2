import User

"""
this class represents an observer that responsible for his owner's notifications.
the observer update his owner's notifications when:
1. other user liked a post of the owner.
2. other user commented on a post of the owner.
3. one of the owner's followed users published a post
"""


class Notifications:
    def __init__(self, owner: User):
        """
        this is a constructor for the observer
        param owner: the observer's owner
        """
        self.owner = owner

    def update_like(self, user):
        """
        this func update the owner's notifications in case that someone liked a post of the owner
        param user: the user who liked the post
        """
        self.owner.my_notifications.append(f"{user.name} liked your post")
        # Add a notification to the post owner notifications list.
        print(f"notification to {self.owner.name}: {user.name} liked your post")

    def update_comment(self, user, information):
        """
          this func update the owner's notifications in case that someone comment on a post of the owner
        param user: the user who commented on the post
        param information: the comment
        """
        self.owner.my_notifications.append(f"{user.name} commented on your post")
        # Add a notification to the post owner notifications list.
        print(f"notification to {self.owner.name}: {user.name} commented on your post: {information}")

    def published_post_notify(self, user):
        """
          this func update the owner's notifications in case that a user followed by the owner published a post
        param user: the user who published a post
        """
        user.my_notifications.append(f"{self.owner.name} has a new post")
        # Add a notification to the user notifications list about the new post.

    def follow_notify(self, other_user):
        print(f"{self.owner.name} started following {other_user.name}")
        # Print a message that the user started following other_user.

    def unfollow_notify(self, other_user):
        print(f"{self.owner.name} unfollowed {other_user.name}")
        # Print a message that the user unfollowed other_user.
