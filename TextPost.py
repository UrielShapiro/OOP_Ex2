from Post import Post


class TextPost(Post):
    def __init__(self, owner, txt):
        self.txt = txt
        super().__init__(owner)

    def __str__(self):  # Default method for printing the post. Changed to match printing current object.
        return f"{self.owner.name} published a post:\n\"{self.txt}\"\n"
