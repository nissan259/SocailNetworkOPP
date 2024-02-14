from post import post


class TextPost(post):
    def __init__(self,user,*args):
        super().__init__(user)
        self.text ,=args[0]
        print( f"{self.user.username} publish  a post {self.text}")


    def __str__(self):
        pass