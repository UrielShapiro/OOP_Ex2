from ImagePost import ImagePost
from Observer import Observer
from SalePost import SalePost
from TextPost import TextPost


def factory_post(post_type: str, owner: 'User', information: str, price, location):
    new_post = None
    if post_type == "Text":
        new_post = TextPost(owner, information)
    elif post_type == "Image":
        new_post = ImagePost(owner, information)
    elif post_type == "Sale":
        new_post = SalePost(owner, information, price, location)
    print(new_post)
    return new_post


class User:
    def __init__(self, name: str, password: str):
        self.name = name
        self.password = password
        self.connected = True
        self.followed = []
        self.my_posts = []
        self.my_notifications = []
        self.followers = []
        self.observer = Observer(self)

    def follow(self, other):
        if self.connected:
            if other in self.followed:
                return
            self.followed.append(other)
            other.followers.append(self)
            print(f"{self.name} started following {other.name}")

    def unfollow(self, other):
        if self.connected:
            if other in self.followed:
                self.followed.remove(other)
                other.followers.remove(self)
                print(f"{self.name} unfollowed {other.name}")

    def log_out(self):
        self.connected = False
        print(f"{self.name} disconnected")

    def log_in(self):
        self.connected = True
        print(f"{self.name} connected")

    def publish_post(self, post_type: str, information: str, price=None, location=None):
        if self.connected:
            new_post = factory_post(post_type, self, information, price, location)
            self.my_posts.append(new_post)
            for user in self.followers:
                self.observer.published_post_notify(user)
            return new_post

    def like_notify(self, other):
        if self.name != other.name:
            self.observer.update_like(other)

    def comment_notify(self, other, inf: str):
        if self.name != other.name:
            self.observer.update_comment(other, inf)

    def print_notifications(self):
        print(f"{self.name}'s notifications:")
        for notification in self.my_notifications:
            print(notification)

    def __str__(self):
        return (f"User name: {self.name}, Number of posts: {self.my_posts.__len__()}, Number of followers: "
                f"{self.followers.__len__()}")
