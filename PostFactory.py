import User
from ImagePost import ImagePost
from Post import Post
from SalePost import SalePost
from TextPost import TextPost


class PostFactory(Post):    # Factory class for creating posts according to the user's choice.
    def getPost(post_type: str, owner: 'User', information: str, price, location):
        new_post = None
        if post_type == "Text":
            new_post = TextPost(owner, information)
        elif post_type == "Image":
            new_post = ImagePost(owner, information)
        elif post_type == "Sale":
            new_post = SalePost(owner, information, price, location)
        print(new_post)
        return new_post
