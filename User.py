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
    this class represents a network's users.
    """

    def __init__(self, name: str, password: str):
        """
        this func is a constructor for a new users.
        receives: name and password of the new users
        """
        self.name = name
        self.password = password
        self.connected = True  # User is created, so it is connected.
        self.iFollow = []  # list of users that this user follows
        self.my_posts = []  # list of posts that this user published
        self.my_notifications = []  # list of notifications that this user received
        self.my_followers = []  # list of users that follow this user
        self.post_factory = single_post_factory()
        # Create a new instance of PostFactory for this user, so that the users could create posts from this class.

    def follow(self, other_user: 'User'):
        """
        this func make the users follow the other users.
        receives: other users to follow
        """
        if self.connected:  # The users can follow other users only if he is connected.
            if other_user in self.iFollow:  # If the users already follow the other users, do nothing.
                return
            # The users doesn't follow the other users, so he would follow him.
            Notifications.notify_follower(self, other_user)  # Notify the other users that this user started following

    def unfollow(self, other_user):
        """
        this func removes the other users from the list of the users who followed by me.
        receives: other users to remove from followed
        """
        if self.connected:  # The users can unfollow other users only if he is connected.
            if other_user in self.iFollow:  # The users would unfollow other_user only if he already follows him.
                Notifications.notify_unfollow(self, other_user)
                # Notify the other users that this user stopped following him.

    def log_in(self):
        """
        this func log in the users(connected -> true)
        """
        self.connected = True  # Change the connected status to True.
        print(f"{self.name} connected")

    def log_out(self):
        """
        this func log out the users(connected -> false)
        """
        self.connected = False  # Change the connected status to False.
        print(f"{self.name} disconnected")

    def publish_post(self, post_type: str, information: str, price=None, location=None):
        """
        this func publishes a post from the users.
        receives: post type (str), information (text for textPost, path for imagePost, description for salePost),
        in case of salePost- price and location to pick up from.
        ** this func uses a factory to return the post of the wanted type. the factory decides which post to create by
        the post type.
        returns: the post of the wanted type.
        """
        if self.connected:  # The users can publish a post only if he is connected.
            new_post = self.post_factory.get_post(post_type, self, information, price, location)
            # Create a new post using the factory method.
            self.my_posts.append(new_post)  # Add the new post to the list of posts that this user published.
            Notifications.published_post_notify(self)
            # Notify all the users that follow this user about the new post.
            return new_post

    def like_notify(self, other):
        """
        this func adds a like for a post.
        receives: the users who made the like and the user's post that was liked (other).
        """
        if self.name != other.name:  # The users can't like his own post.
            Notifications.update_like(self, other)  # Notify the post-owner that this user liked his post.

    def comment_notify(self, other, info: str):
        """
        this func adds a comment for a post
        param other: the users who commented
        param info: the comment
        """
        if self.name != other.name:  # The users can't comment on his own post.
            Notifications.update_comment(self, other, info)
            # Notify the post-owner that this user commented on his post.
            # Include the information of the comment in the notification.

    def print_notifications(self):
        """
        this func prints the user's notifications
        """
        print(f"{self.name}'s notifications:")
        for notification in self.my_notifications:
            # Go over all the notifications that this user received (stored in the user's notification list) and
            # print them.
            print(notification)

    def __str__(self):
        """
        this func is a Default print method to print the user's parameters.
        """
        return (f"User name: {self.name}, Number of posts: {self.my_posts.__len__()}, Number of followers: "
                f"{self.my_followers.__len__()}")
