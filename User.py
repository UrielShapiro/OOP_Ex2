from Notifications import Notifications
import Post


class User:
    """
    this class represent a network's user.
    """

    def __init__(self, name: str, password: str):
        """this func is a constructor for a new user.
        receives: name and password of the new user
        """
        self.name = name
        self.password = password
        self.connected = True  # User is created, so it is connected.
        self.iFollow = []  # list of users that this user follows
        self.my_posts = []  # list of posts that this user published
        self.my_notifications = []  # list of notifications that this user received
        self.followers = []  # list of users that follow this user
        self.observer_notifications = Notifications(self)

    def follow(self, other_user: 'User'):
        """
        this func make the user follow the other user.
        receives: other user to follow
        """
        if self.connected:  # The user can follow other users only if he is connected.
            if other_user in self.iFollow:  # If the user already follows the other user, do nothing.
                return
            # The user doesn't follow the other user, so he would follow him.
            self.observer_notifications.follow_notify(other_user)

    def unfollow(self, other_user):
        """
        this func remove the other user from the list of the users who followed by self.
        receives: other user to remove from followed
        """
        if self.connected:  # The user can unfollow other users only if he is connected.
            if other_user in self.iFollow:  # The user would unfollow other_user only if he already follows him.
                self.observer_notifications.unfollow_notify(other_user)

    def log_in(self):
        """
        this func log in the user(connected -> true)
        """
        self.connected = True  # Change the connected status to True.
        print(f"{self.name} connected")

    def log_out(self):
        """
        this func log out the user(connected -> false)
        """
        self.connected = False  # Change the connected status to False.
        print(f"{self.name} disconnected")

    def publish_post(self, post_type: str, information: str, price=None, location=None):
        """
        this func publishes a post from the user.
        receives: post type (str), information (text for textPost, path for imagePost, description for salePost),
        in case of salePost- price and location to pick up from.
        ** this func uses a factory to return the post of the wanted type. the factory decides which post to create by
        the post type.
        returns: the post of the wanted type.
        """
        if self.connected:  # The user can publish a post only if he is connected.
            new_post = Post.get_post(post_type, self, information, price, location)
            # Create a new post using the factory method.
            self.my_posts.append(new_post)  # Add the new post to the list of posts that this user published.
            for user in self.followers:
                self.observer_notifications.published_post_notify(user)
                # Notify all the users that follow this user about the new post.
            return new_post

    def like_notify(self, other):
        """
        this func add a like for a post.
        receives: the user who made the like
        """
        if self.name != other.net_name:  # The user can't like his own post.
            self.observer_notifications.update_like(other)  # Notify the post owner that this user liked his post.

    def comment_notify(self, other, inf: str):
        """
        this func add a comment for a post
        param other: the user who commented
        param inf: the comment
        """
        if self.name != other.net_name:  # The user can't comment on his own post.
            self.observer_notifications.update_comment(other, inf)
            # Notify the post owner that this user commented on his post.
            # Include the information of the comment in the notification.

    def print_notifications(self):
        """
        this func print the user's notifications
        """
        print(f"{self.name}'s notifications:")
        for notification in self.my_notifications:
            # Go over all the notifications that this user received (stored in the user's notification list) and
            # print them.
            print(notification)

    def __str__(self):
        """
        this func is a Default print method to print the user parameters.
        """
        return (f"User name: {self.name}, Number of posts: {self.my_posts.__len__()}, Number of followers: "
                f"{self.followers.__len__()}")
