from Post import Post


class SalePost(Post):
    def __init__(self, owner, inf, price, location):
        self.inf = inf
        self.price = price
        self.location = location
        self.isAvailable = True
        super().__init__(owner)

    def __str__(self):
        if self.isAvailable:
            return (f"{self.owner.name} posted a product for sale:\nFor sale! {self.inf}, price: {self.price}, "
                    f"pickup from: {self.location}\n")
        else:
            return (f"{self.owner.name} posted a product for sale:\nSold! {self.inf}, price: {self.price}, "
                    f"pickup from: {self.location}\n")

    def discount(self, percent, password):
        if self.owner.connected is True and self.owner.password == password:
            self.price -= self.price * percent / 100
            print(f"Discount on {self.owner.name} product! the new price is: {self.price}")

    def sold(self, password: str):
        if self.owner.connected is True and self.owner.password == password:
            self.isAvailable = False
            print(f"{self.owner.name}'s product is sold")
