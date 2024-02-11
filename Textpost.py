from Post import Post


class TextPost(Post):
    def __init__(self, owner, txt):
        self.txt = txt
        super().__init__(owner)

    def print_post(self):
        print(self.owner.name + " published a post:\n" + self.txt)
