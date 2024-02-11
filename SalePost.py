from Post import Post


class SalePost(Post):
    def __init__(self, owner, inf, price, location, isAvailable=True):
        self.inf = inf
        self.price = price
        self.location = location
        self.isAvailable = isAvailable
        super().__init__(owner)

    def discount(self, percent, password):
        if self.owner.connect is True and self.owner.password == password:
            self.price -= self.price * percent / 100

    def sold(self, password):
        if self.owner.connect is True and self.owner.password == password:
            self.isAvailable = False

    def print_post(self):
        print(self.owner.name + " posted a product for sale:\nFor sale!" + self.inf + ", price: " + self.price + ", pickup from: " + self.location)
