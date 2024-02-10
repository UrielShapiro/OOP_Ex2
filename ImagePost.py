import PIL.Image
from Post import Post


class ImagePost(Post):
    def __init__(self, owner, path):
        self.path = path
        super().__init__(owner)

    def display(self):
        img = PIL.Image.open(self.path)
