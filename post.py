from abc import ABC, abstractmethod


class post(ABC):
    def __init__(self, user):
        self.how_like = set()
        self.user = user
        self.comments = []

    def like(self, user):
        # use set beacuse i want to prevent duplicate like
        self.how_like.add(user)

    def unlike(self, user):
        # use set beacuse i want to prevent duplicate like
        self.how_like.remove(user)

    def add_comment(self, user, comment):
        # use at dictonrt the key: user value:comment
        self.comments.append(user)
        self.notifications.append(user.username, "commendet on your post")

    @abstractmethod
    def __str__(self):
        pass
