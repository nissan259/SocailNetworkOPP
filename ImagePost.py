from post import post
import matplotlib.pyplot as plt

class ImagePost(post):
    def __init__(self,user,*args):
        super().__init__(user)
        temp ,=args[0] # unpack the the args
        self.image =temp  # unpack the the args

    def __str__(self):
        pass

    def display(self):

        image_rgb = plt.imread(self.image)
        plt.imshow(image_rgb)
        plt.axis('off')
        plt.show()

