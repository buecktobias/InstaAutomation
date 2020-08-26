from instaapi import InstaAPI
from user import User
from threading import Thread
from trigger import EbayTrigger
from datetime import timedelta
from ebayAPI import EbayAPI
from post import Post
from PIL import Image, ImageDraw, ImageFont

class Automation:
    def __init__(self, name, trigger_object):
        self.trigger_object = trigger_object
        self.insta_api = InstaAPI()
        self.user = User(name)

    def post(self, post):
        self.insta_api.login(self.user.user_name, self.user.password)
        self.insta_api.post(post.image_path, post.caption)

    def run(self):
        self.trigger_object.run()

    def trigger(self):
        pass


class EbayAutomation(Automation):
    def __init__(self, name, city):
        super().__init__(name, EbayTrigger(timedelta(seconds=10), self))
        self.city = city
        self.hashtags = ["#ebay"]

    def trigger(self):
        #try:
            eb = EbayAPI().search(self.city)
            img_path = eb.get_image()

            img = Image.open(img_path)
            d1 = ImageDraw.Draw(img)
            d1.text((20, 20), "Hello, TutorialsPoint!", fill=(255, 0, 0))
            img.save(img_path)

            hashtags = self.hashtags + list(map(lambda x: "#" + x, eb.title.split(" ")))
            hashtags_string = " ".join(hashtags)
            text = eb.title + f"\n Ebay: {eb.ebay_link} \n\n {hashtags_string}"
            post = Post(text, img_path)
            self.post(post)
            self.insta_api.reset_browser()
        #except Exception as e:
         #   print(e)


if __name__ == '__main__':
    ea = EbayAutomation("ebayBot", "Mainz")
    ea.run()
