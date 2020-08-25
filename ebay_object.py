from dataclasses import dataclass
import urllib.request
import random


@dataclass
class EbayObject:
    image_src: str
    title: str
    ebay_link: str

    def get_image(self):
        print('Beginning file download with urllib2...')
        url = self.image_src
        if self.title == "":
            self.title = str(random.randint(0, 100_000))
        path = f"/home/tobias/Pictures/ebay/{str(random.randint(0, 100_000_000_000_000))}.jpg"
        urllib.request.urlretrieve(url, path)
        return path


if __name__ == '__main__':
    EbayObject("https://i.ebayimg.com/00/s/MTYwMFg5MDA=/z/Cb4AAOSw-nRfRO8C/$_2.JPG", "HAHAH XDDD", "").get_image()
