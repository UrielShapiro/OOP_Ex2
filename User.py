from Notifications import Notifications
from Post import PostFactory

_factory = None  # Wll be used to create only one instance of the PostFactory.


def single_post_factory():
    """
    this func is a singleton for the post factory.
    Was created only for storage efficiency. because it doesn't really matter if we create multiple instances of
    the post factory.
    :return:
    """
    global _factory  # This function changes the global variable _factory.
    if _factory is None:  # If the _factory is not created, create it.
        _factory = PostFactory()  # Create a new instance of PostFactory.
    return _factory


class User:
    """
    this class represent a network's user.
    """

    def __init__(self, name: str, password: str):
        """
        this func is a constructor for a new user.
        receives: name and password of the new user
        """
        self.name = name
        self.password = password
        self.connected = True  # User is created, so it is connected.
        self.iFollow = []  # list of users that this user follows
        self.my_posts = []  # list of posts that this user published
        self.my_notifications = []  # list of notifications that this user received
        self.my_followers = []  # list of users that follow this user
        self.observer_notifications = Notifications(self)  # Create a new instance of Notifications for this user.
        self.post_factory = single_post_factory()
        # Create a new instance of PostFactory for this user, so that the user could create posts from this class.

    def follow(self, other_user: 'User'):
        """
        this func make the user follow the other user.
        receives: other user to follow
        """
        if self.connected:  # The user can follow other users only if he is connected.
            if other_user in self.iFollow:  # If the user already follows the other user, do nothing.
                return
            # The user doesn't follow the other user, so he would follow him.
            Notifications.notify_follower(self, other_user)  # Notify the other user that this user started following

    def unfollow(self, other_user):
        """
        this func remove the other user from the list of the users who followed by self.
        receives: other user to remove from followed
        """
        if self.connected:  # The user can unfollow other users only if he is connected.
            if other_user in self.iFollow:  # The user would unfollow other_user only if he already follows him.
                Notifications.notify_unfollow(self, other_user)
                # Notify the other user that this user stopped following him.

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
            new_post = self.post_factory.get_post(post_type, self, information, price, location)
            # Create a new post using the factory method.
            self.my_posts.append(new_post)  # Add the new post to the list of posts that this user published.
            Notifications.published_post_notify(self)
            # Notify all the users that follow this user about the new post.
            return new_post

    def like_notify(self, other):
        """
        this func add a like for a post.
        receives: the user who made the like
        """
        if self.name != other.name:  # The user can't like his own post.
            self.observer_notifications.update_like(other)  # Notify the post owner that this user liked his post.

    def comment_notify(self, other, info: str):
        """
        this func add a comment for a post
        param other: the user who commented
        param info: the comment
        """
        if self.name != other.name:  # The user can't comment on his own post.
            self.observer_notifications.update_comment(other, info)
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
                f"{self.my_followers.__len__()}")
