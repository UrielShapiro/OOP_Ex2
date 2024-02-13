import User
from ImagePost import ImagePost
from SalePost import SalePost
from Textpost import TextPost


def factory_post(postType: str, owner: 'User', information: str, price, location):
    if postType == "Text":
        return TextPost(owner, information)
    elif postType == "Image":
        return ImagePost(owner, information)
    elif postType == "Sale":
        return SalePost(owner, information, price, location)


class Post:
    def __init__(self, owner):
        self.owner = owner

    ######################
    # def like(self, user):
    #     self.owner.like_notify(user)
    #
    # def comment(self, user, txt):
    #     self.owner.comment_notify(user, txt)
