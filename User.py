from Post import Post


class User:
    followed = []
    my_posts = []
    my_notifications = []

    def __init__(self, name, password, isConnect):
        self.name = name
        self.password = password
        self.connect = isConnect

    def follow(self, other):
        if self.connect:
            for f in self.followed:
                if f.name == other.name:
                    return
            self.followed.append(other)

    def unfollow(self, other):
        if self.connect:
            for f in self.followed:
                if f.name == other.name:
                    self.followed.remove(other)

    def log_out(self):
        self.connect = False

    def log_in(self):
        self.connect = True

    def publish_post(self, ty, inf, price=None, location=None, isAvailable=True):
        if self.connect:
            ps = Post(...)
            self.my_posts.append(ps)
            # if ty == "Text":
            #     self.my_posts.append(TextPost(self, inf))
            # elif ty == "Image":
            #     self.my_posts.append(ImagePost(self, inf))
            # elif ty == "Sale":
            #     self.my_posts.append(SalePost(self, inf, price, location, isAvailable))

    ##################################################
    def print_notifications(self):
        pass
