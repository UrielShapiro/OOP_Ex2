from Post import Post


class SalePost(Post):
    def __init__(self, owner, inf, price, location):
        self.inf = inf
        self.price = price
        self.location = location
        self.isAvailable = True         # When creating a new post, the product is available.
        super().__init__(owner)

    def __str__(self):  # Default method for printing the post. Changed to match printing current object.
        if self.isAvailable:    # If the product is available, the post will show that it is for sale.
            return (f"{self.owner.name} posted a product for sale:\nFor sale! {self.inf}, price: {self.price}, "
                    f"pickup from: {self.location}\n")
        else:                   # If the product is not available, the post will show that it is sold.
            return (f"{self.owner.name} posted a product for sale:\nSold! {self.inf}, price: {self.price}, "
                    f"pickup from: {self.location}\n")

    def discount(self, percent, password):
        if self.owner.connected is True and self.owner.password == password:
            # If the user is connected and his password matches the input password, he can discount the product.
            self.price -= self.price * percent / 100    # Calculate the new price after the discount.
            print(f"Discount on {self.owner.name} product! the new price is: {self.price}")

    def sold(self, password: str):
        if self.owner.connected is True and self.owner.password == password:
            # If the user is connected and his password matches the input password, he can sell the product.
            self.isAvailable = False    # Change the product status to not available.
            print(f"{self.owner.name}'s product is sold")
