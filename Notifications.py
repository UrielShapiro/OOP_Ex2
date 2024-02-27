import User

"""
this class represents an observer that responsible for his owner's notifications.
the observer update his owner's notifications when:
1. other user liked a post of the owner.
2. other user commented on a post of the owner.
3. one of the owner's followed users published a post
"""


class Notifications:
    # def __init__(me, owner: User):
    #     """
    #     this is a constructor for the observer
    #     param owner: the observer's owner
    #     """
    #     me.owner = owner
    @staticmethod
    def update_like(me, user):
        """
        this func updates the owner's notifications in case that someone liked a post of the owner
        param user: the user who liked the post
        """
        me.my_notifications.append(f"{user.name} liked your post")
        # Add a notification to the post-owner notifications list.
        print(f"notification to {me.name}: {user.name} liked your post")

    @staticmethod
    def update_comment(me, user, information):
        """
        this func updates the owner's notifications in case that someone comments on a post of the owner
        param user: the user who commented on the post
        param information: the comment
        """
        me.my_notifications.append(f"{user.name} commented on your post")
        # Add a notification to the post-owner notifications list.
        print(f"notification to {me.name}: {user.name} commented on your post: {information}")

    @staticmethod
    def published_post_notify(me: User):
        """
          this func updates the owner's notifications in case that a user followed by the owner published a post
        param user: the user who published a post
        """
        for user in me.my_followers:  # Go over all the users that follow this user.
            user.my_notifications.append(f"{me.name} has a new post")
            # Add a notification to the user notifications list about the new post.

    @staticmethod
    def notify_follower(me: User, other_user):
        """
        This func updates the owner's notifications in case that a user followed by the owner published a post
        :param other_user: The user "me" started following
        :param me: the user who follows
        """
        me.iFollow.append(other_user)  # Add the other user to the list of users that this user follows.
        other_user.my_followers.append(me)  # Add this user to the list of users that follow the other user.
        print(f"{me.name} started following {other_user.name}")
        # Print a message that the user started following other_user.

    @staticmethod
    def notify_unfollow(me: User, other_user):
        """
        This func updates the owner's notifications in case that a user followed by the owner published a post
        :param other_user: The user "me" started following
        :param me: the user who follows
        """
        me.iFollow.remove(other_user)  # Remove the other_user from the list of users that this user follows.
        other_user.my_followers.remove(me)  # Remove this user from the list of users that follow the
        # other_user.
        print(f"{me.name} unfollowed {other_user.name}")    # Print a message that the user unfollowed other_user.
