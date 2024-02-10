from Post import Post


class TextPost(Post):
    def __init__(self, owner, txt):
        self.txt = txt
        super().__init__(owner)
