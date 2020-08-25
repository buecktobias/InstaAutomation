from instaapi import InstaAPI
from user import User


class Automation:
    def __init__(self, name):
        self.insta_api = InstaAPI()
        self.user = User(name)

    def post(self, post):
        self.insta_api.login(self.user.user_name, self.user.password)
        self.insta_api.post(post.image_path, post.caption)


    def trigger(self):
        pass


class EbayAutomation(Automation):
    def __init__(self, name, city):
        super().__init__(name)
        self.city = city
    def trigger(self):

