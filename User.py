import Post
from ImagePost import ImagePost
from SalePost import SalePost
from Textpost import TextPost


class User:
    followed = []
    my_posts = []
    my_notifications = []
    followers = []

    def __init__(self, name: str, password: str, isConnected: bool):
        self.name = name
        self.password = password
        self.connected = isConnected

    def follow(self, other):
        if self.connected:
            for f in self.followed:
                if f.name == other.name:
                    return
            self.followed.append(other)
            other.followers.append(self)
            print(f"{other.name} started following {self.name}")

    def unfollow(self, other):
        if self.connected:
            for f in self.followed:
                if f.name == other.name:
                    self.followed.remove(other)
                    other.followers.remove(self)
                    print(f"{self.name} unfollowed {other.name}")

    def log_out(self):
        self.connected = False
        print(f"{self.name} disconnected")

    def log_in(self):
        self.connected = True
        print(f"{self.name} connected")

    def publish_post(self, postType: str, information: str, price=None, location=None):
        if self.connected:
            new_post = Post.factory_post(postType, self, information, price, location)
            self.my_posts.append(new_post)
            return new_post

    def __str__(self):
        return (f"User name: {self.name} ,Number of posts: {self.my_posts.__len__()}, Number of followers: "
                f"{self.followers.__len__()}")

    # def like_notify(self, other: 'User'):
    #     observer.updat_like(self, other)
    #
    # def print_notifications(self):
    #     pass
