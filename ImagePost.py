from Post import Post
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class ImagePost(Post):
    def __init__(self, owner, path):
        self.path = path
        super().__init__(owner)

    def __str__(self):  # Default method for printing the post. Changed to match printing current object.
        return f"{self.owner.name} posted a picture\n"

    def display(self):          # Function to display the picture. uses matplotlib library.
        print("Shows picture")
        try:
            img = mpimg.imread(self.path)   # Read the image from the path.
            plt.imshow(img)                 # Show the image.
            plt.axis("off")
            plt.show()
        except FileNotFoundError:   # If the file is not found, don't crash the program.
            pass

