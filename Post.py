import User
from enum import Enum
from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class Post(ABC):
    """
    this class is the parent of all the posts. All the posts inherits this class.
    """

    def __init__(self, owner):
        """
        this func is a constructor for a post
        param owner: the post's owner
        """
        self.owner = owner

    def like(self, user: 'User'):
        """
        this func is used when a users like a post.
        this func notify the post's owner about the like using the owner's observer.
        param users: the users who liked the post.
        """
        self.owner.like_notify(user)  # If users like a post, the post-owner will be notified.

    def comment(self, user: User, txt: str):
        """
        this func is used when users comment on a post.
        this func notifies the post's owner about the comment using the owner's observer.
        param users: the users who commented on the post.
        """
        self.owner.comment_notify(user, txt)  # If users comment on a post, the post-owner will be notified.

    @abstractmethod
    def __str__(self):
        """
        each post type has a different string representation and will need to override this method.
        """
        pass


class ImagePost(Post):
    """
    this class represent an image post type.
    """

    def __init__(self, owner, path):
        """
        this func is a constructor for the image post.
        param owner: the users who published the post
        param path: the path to the picture
        """
        self.path = path
        super().__init__(owner)

    def __str__(self):
        """
        this is a Default method for printing the post. Changed to match printing current object.
        """
        return f"{self.owner.name} posted a picture\n"

    def display(self):
        """
        this function is used to display the picture. uses matplotlib library.
        """
        print("Shows picture")
        try:
            img = mpimg.imread(self.path)  # Read the image from the path.
            plt.imshow(img)  # Show the image.
            plt.axis("off")
            plt.show()
        except FileNotFoundError:  # If the file is not found, don't crash the program.
            pass


class SalePost(Post):
    """
    this class represent a sale post type.
    """

    def __init__(self, owner, inf, price, location):
        """
        this func is a constructor for the sale post.
        param owner: the users who published the post
        param inf: the product's details
        param price: the product's price
        param location: the location to pick up the product
        """
        self.inf = inf
        self.price = price
        self.location = location
        self.isAvailable = True  # When creating a new post, the product is available.
        super().__init__(owner)

    def __str__(self):
        """
        this is a default method for printing the post. Changed to match printing SalePost.
        """
        if self.isAvailable:  # If the product is available, the post will show that it is for sale.
            return (f"{self.owner.name} posted a product for sale:\nFor sale! {self.inf}, price: {self.price}, "
                    f"pickup from: {self.location}\n")
        else:  # If the product is not available, the post will show that it is sold.
            return (f"{self.owner.name} posted a product for sale:\nSold! {self.inf}, price: {self.price}, "
                    f"pickup from: {self.location}\n")

    def discount(self, percent, password):
        """
        this func is used when the post's owner want to discount the product's price.
        param percent: the amount of discount in precedent.
        param password: the post's owner password
        """
        if self.owner.connected is True and self.owner.password == password:
            # If the users is connected and his password matches the input password, he can discount the product.
            self.price -= self.price * percent / 100  # Calculate the new price after the discount.
            print(f"Discount on {self.owner.name} product! the new price is: {self.price}")

    def sold(self, password: str):
        """
        this func is used when the post's owner want to declare on the product as "sold".
        param password: the post's owner password.
        """
        if self.owner.connected is True and self.owner.password == password:
            # If the users is connected and his password matches the input password, he can sell the product.
            self.isAvailable = False  # Change the product status to not available.
            print(f"{self.owner.name}'s product is sold")


class TextPost(Post):
    """
    this class represent a text post type.
    """

    def __init__(self, owner, txt):
        """
         this func is a constructor for the sale post.
        param owner: the users who published the post
        param txt: the text of the post.
        """
        self.txt = txt
        super().__init__(owner)

    def __str__(self):
        """
        this is a default method for printing the post. Changed to match printing current object.
        """
        return f"{self.owner.name} published a post:\n\"{self.txt}\"\n"


class PostType(Enum):
    """
    this is an enum class that represents the post's types for easy modification when updating the code.
    """
    Text = "Text"
    Image = "Image"
    Sale = "Sale"


class PostFactory:

    @staticmethod
    def get_post(post_type: str, owner: 'User', information: str, price, location):
        """
        this is a factory that creates for the users a post from the wanted type.
        param post_type: the wanted type of the post
        param owner: the post's owner.
        param information: text post-the text, image post-the path to the image, sale post-the product's details.
        param price: (if the post is a sale post) the product's price
        param location: (if the post is a sale post) location to pick up from
        return: anew post of the wanted type.
        """
        new_post = None
        if post_type == PostType.Text.value:
            new_post = TextPost(owner, information)
        elif post_type == PostType.Image.value:
            new_post = ImagePost(owner, information)
        elif post_type == PostType.Sale.value:
            new_post = SalePost(owner, information, price, location)
        print(new_post)
        return new_post
