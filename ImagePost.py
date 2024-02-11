from Post import Post
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class ImagePost(Post):
    def __init__(self, owner, path):
        self.path = path
        super().__init__(owner)



    def display(self):
        try:
            img = mpimg.imread(self.path)
            plt.imshow(img)
            plt.axis("off")  # Hide axes
            plt.show()
            print("Shows picture")
        except FileNotFoundError:
            print(f"Image not found at path: {self.path}")


