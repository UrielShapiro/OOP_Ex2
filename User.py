from ImagePost import ImagePost
from SalePost import SalePost
from TextPost import TextPost


def factory_post(post_type: str, owner: 'User', information: str, price=None, location=None):
    if post_type == "Text":
        return TextPost(owner, information)
    elif post_type == "Image":
        return ImagePost(owner, information)
    elif post_type == "Sale":
        return SalePost(owner, information, price, location)


class User:
    IFollow = []
    my_posts = []
    my_notifications = []
    FollowMe = []

    def __init__(self, name: str, password: str):
        self.name = name
        self.password = password
        self.connected = True

    def follow(self, other):
        if self.connected:
            for user in self.IFollow:
                if user.name == other.name:
                    return
            self.IFollow.append(other)
            other.FollowMe.append(self)
            print(f"{self.name} started following {other.name}")

    def unfollow(self, other):
        if self.connected:
            for f in self.IFollow:
                if f.name == other.name:
                    self.IFollow.remove(other)
                    other.FollowMe.remove(self)
                    print(f"{self.name} unfollowed {other.name}")

    def log_out(self):
        self.connected = False
        print(f"{self.name} disconnected")

    def log_in(self):
        self.connected = True
        print(f"{self.name} connected")

    # def publish_post(self, postType: str, information: str, price=None, location=None):
    #     if self.connected:
    #         if postType == "Text":
    #             self.my_posts.append(TextPost(self, information))
    #             print(f"{self.name} published a post:\n {information}")
    #         elif postType == "Image":
    #             self.my_posts.append(ImagePost(self, information))
    #             print(f"{self.name} posted a picture")
    #         elif postType == "Sale":
    #             self.my_posts.append(SalePost(self, information, price, location))
    #             print(
    #                 f"{self.name} posted a product for sale:\nFor sale! {information}, price: {price}  "
    #                 f"pickup from: {location}")

    def publish_post(self, postType: str, information: str, price=None, location=None):
        if self.connected:
            new_post = factory_post(postType, self, information, price, location)
            self.my_posts.append(new_post)
            return new_post

    def __str__(self):
        return (f"User name: {self.name} ,Number of posts: {self.my_posts.__len__()}, Number of followers: "
                f"{self.FollowMe.__len__()}")

    ##################################################
    def print_notifications(self):
        pass
