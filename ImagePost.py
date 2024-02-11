# import PIL.Image
from Post import Post


class ImagePost(Post):
    def __init__(self, owner, path):
        self.path = path
        super().__init__(owner)

    def print_post(self):
        print(self.owner.name+ "posted a picture")

##################################
    # def display(self):
    #     img = PIL.Image.open(self.path)
