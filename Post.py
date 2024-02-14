import User
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class Post:
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
        this func is used when a user like a post.
        this func notify the post's owner about the like using the owner's observer.
        param user: the user who liked the post.
        """
        self.owner.like_notify(user)  # If a user likes a post, the post owner will be notified.

    def comment(self, user: User, txt: str):
        """
        this func is used when a user comments on a post.
        this func notify the post's owner about the comment using the owner's observer.
        param user: the user who commented on the post.
        """
        self.owner.comment_notify(user, txt)  # If a user comments on a post, the post owner will be notified.


class ImagePost(Post):
    """
    this class represent an image post type.
    """
    def __init__(self, owner, path):
        """
        this func is a constructor for the image post.
        param owner: the user who published the post
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

    """
    def __init__(self, owner, inf, price, location):
        self.inf = inf
        self.price = price
        self.location = location
        self.isAvailable = True  # When creating a new post, the product is available.
        super().__init__(owner)

    def __str__(self):  # Default method for printing the post. Changed to match printing current object.
        if self.isAvailable:  # If the product is available, the post will show that it is for sale.
            return (f"{self.owner.name} posted a product for sale:\nFor sale! {self.inf}, price: {self.price}, "
                    f"pickup from: {self.location}\n")
        else:  # If the product is not available, the post will show that it is sold.
            return (f"{self.owner.name} posted a product for sale:\nSold! {self.inf}, price: {self.price}, "
                    f"pickup from: {self.location}\n")

    def discount(self, percent, password):
        if self.owner.connected is True and self.owner.password == password:
            # If the user is connected and his password matches the input password, he can discount the product.
            self.price -= self.price * percent / 100  # Calculate the new price after the discount.
            print(f"Discount on {self.owner.name} product! the new price is: {self.price}")

    def sold(self, password: str):
        if self.owner.connected is True and self.owner.password == password:
            # If the user is connected and his password matches the input password, he can sell the product.
            self.isAvailable = False  # Change the product status to not available.
            print(f"{self.owner.name}'s product is sold")


class TextPost(Post):
    def __init__(self, owner, txt):
        self.txt = txt
        super().__init__(owner)

    def __str__(self):  # Default method for printing the post. Changed to match printing current object.
        return f"{self.owner.name} published a post:\n\"{self.txt}\"\n"


def get_post(post_type: str, owner: 'User', information: str, price, location):
    new_post = None
    if post_type == "Text":
        new_post = TextPost(owner, information)
    elif post_type == "Image":
        new_post = ImagePost(owner, information)
    elif post_type == "Sale":
        new_post = SalePost(owner, information, price, location)
    print(new_post)
    return new_post
