import User
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class Post:
    def __init__(self, owner):
        self.owner = owner

    def like(self, user: 'User'):
        self.owner.like_notify(user)  # If a user likes a post, the post owner will be notified.

    def comment(self, user: User, txt: str):
        self.owner.comment_notify(user, txt)  # If a user comments on a post, the post owner will be notified.


class ImagePost(Post):
    def __init__(self, owner, path):
        self.path = path
        super().__init__(owner)

    def __str__(self):  # Default method for printing the post. Changed to match printing current object.
        return f"{self.owner.name} posted a picture\n"

    def display(self):  # Function to display the picture. uses matplotlib library.
        print("Shows picture")
        try:
            img = mpimg.imread(self.path)  # Read the image from the path.
            plt.imshow(img)  # Show the image.
            plt.axis("off")
            plt.show()
        except FileNotFoundError:  # If the file is not found, don't crash the program.
            pass


class SalePost(Post):
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
