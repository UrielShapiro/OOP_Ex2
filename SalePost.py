from Post import Post


class SalePost(Post):
    def __init__(self, owner, inf, price, location, isAvailable=True):
        self.inf = inf
        self.price = price
        self.location = location
        self.isAvailable = isAvailable
        super().__init__(owner)
