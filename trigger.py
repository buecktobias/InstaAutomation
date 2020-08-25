import datetime
import time
from datetime import timedelta
import abc
import threading
from automation import Automation


class Trigger(abc.ABC, threading.Thread):
    def __init__(self, interval: timedelta, trigger_object: Automation):
        super().__init__()
        self.interval = interval
        self.triger_object = trigger_object

    def run(self):
        while True:
            time.sleep(self.interval.seconds)
            if self.test():
                self.triger_object.trigger()

    @abc.abstractmethod
    def test(self):
        pass


class EbayTrigger(Trigger):
    def test(self):
        # new ebay post ?
        return True


if __name__ == '__main__':
    et = EbayTrigger(timedelta(seconds=2), Automation())
    et.start()



