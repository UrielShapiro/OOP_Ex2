from Post import Post


class SalePost(Post):
    def __init__(self, owner, inf, price, location):
        self.inf = inf
        self.price = price
        self.location = location
        self.isAvailable = True
        super().__init__(owner)

    def __str__(self):
        return (f"{self.owner.name} posted a product for sale:\nFor sale! {self.inf}, price: {self.price}, "
                f"pickup from: {self.location}")

    def discount(self, percent, password):
        if self.owner.connected is True and self.owner.password == password:
            self.price -= self.price * percent / 100
            print(f"Discount on {self.owner} product! the new price is: {self.price}")

    def sold(self, password):
        if self.owner.connected is True and self.owner.password == password:
            self.isAvailable = False
            print(f"{self.owner} product is sold")
