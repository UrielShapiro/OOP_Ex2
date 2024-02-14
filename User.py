from Notifications import Notifications
from Post import get_post

""""""
class User:
    def __init__(self, name: str, password: str):
        self.name = name
        self.password = password
        self.connected = True        # User is created, so it is connected.
        self.iFollow = []            # list of users that this user follows
        self.my_posts = []           # list of posts that this user published
        self.my_notifications = []   # list of notifications that this user received
        self.followers = []          # list of users that follow this user
        self.observer_notifications = Notifications(self)

    def follow(self, other_user: 'User'):
        if self.connected:              # The user can follow other users only if he is connected.
            if other_user in self.iFollow:   # If the user already follows the other user, do nothing.
                return
            # The user doesn't follow the other user, so he would follow him.
            self.iFollow.append(other_user)      # Add the other user to the list of users that this user follows.
            other_user.followers.append(self)    # Add this user to the list of users that follow the other user.
            print(f"{self.name} started following {other_user.name}")
            # Print a message that the user started following other_user.

    def unfollow(self, other_user):
        if self.connected:                  # The user can unfollow other users only if he is connected.
            if other_user in self.iFollow:       # The user would unfollow other_user only if he already follows him.
                self.iFollow.remove(other_user)  # Remove the other_user from the list of users that this user follows.
                other_user.followers.remove(self)  # Remove this user from the list of users that follow the other_user.
                print(f"{self.name} unfollowed {other_user.name}")
                # Print a message that the user unfollowed other_user.

    def log_out(self):
        self.connected = False  # Change the connected status to False.
        print(f"{self.name} disconnected")

    def log_in(self):
        self.connected = True   # Change the connected status to True.
        print(f"{self.name} connected")

    def publish_post(self, post_type: str, information: str, price=None, location=None):
        if self.connected:        # The user can publish a post only if he is connected.
            new_post = get_post(post_type, self, information, price, location)
            # Create a new post using the factory method.
            self.my_posts.append(new_post)  # Add the new post to the list of posts that this user published.
            for user in self.followers:
                self.observer_notifications.published_post_notify(user)
                # Notify all the users that follow this user about the new post.
            return new_post

    def like_notify(self, other):
        if self.name != other.name:             # The user can't like his own post.
            self.observer_notifications.update_like(other)    # Notify the post owner that this user liked his post.

    def comment_notify(self, other, inf: str):
        if self.name != other.name:                     # The user can't comment on his own post.
            self.observer_notifications.update_comment(other, inf)
            # Notify the post owner that this user commented on his post.
            # Include the information of the comment in the notification.

    def print_notifications(self):
        print(f"{self.name}'s notifications:")
        for notification in self.my_notifications:
            # Go over all the notifications that this user received (stored in the user's notification list) and
            # print them.
            print(notification)

    def __str__(self):  # Default print method to print the user parameters.
        return (f"User name: {self.name}, Number of posts: {self.my_posts.__len__()}, Number of followers: "
                f"{self.followers.__len__()}")
