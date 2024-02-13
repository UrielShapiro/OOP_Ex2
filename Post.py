# import User
# import ImagePost
# import SalePost
# import Textpost

#
# def factory_post(postType: str, owner: 'User', information: str, price, location):
#     if postType == "Text":
#         return Textpost.TextPost(owner, information)
#     elif postType == "Image":
#         return ImagePost.ImagePost(owner, information)
#     elif postType == "Sale":
#         return SalePost.SalePost(owner, information, price, location)


class Post:
    def __init__(self, owner):
        self.owner = owner

    ######################
    # def like(self, user):
    #     self.owner.like_notify(user)
    #
    # def comment(self, user, txt):
    #     self.owner.comment_notify(user, txt)
