from Post import Post


class SalePost(Post):
    def __init__(self, owner, information, price, location):
        self.information = information
        self.price = price
        self.location = location
        self.isAvailable = True
        super().__init__(owner)
        print(
            f"{owner.name} posted a product for sale:\nFor sale! {information}, price: {price}  "
            f"pickup from: {location}")

    def discount(self, percent, password):
        if self.owner.connected is True and self.owner.password == password:
            self.price -= self.price * percent / 100
            print(f"Discount on {self.owner} product! the new price is: {self.price}")

    def sold(self, password):
        if self.owner.connected is True and self.owner.password == password:
            self.isAvailable = False
            print(f"{self.owner} product is sold")

