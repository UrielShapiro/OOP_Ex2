from Post import Post
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class ImagePost(Post):
    def __init__(self, owner, path):
        self.path = path
        super().__init__(owner)

    def __str__(self):
        return f"{self.owner.name} posted a picture\n"

    def display(self):
        print("Shows picture")
        try:
            img = mpimg.imread(self.path)
            plt.imshow(img)
            plt.axis("off")
            plt.show()
        except FileNotFoundError:
            pass

