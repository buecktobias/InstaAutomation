import time
from datetime import timedelta
import abc


class Trigger(abc.ABC):
    def __init__(self, interval: timedelta, trigger_object):
        super().__init__()
        self.interval = interval
        self.triger_object = trigger_object

    def run(self):
        self.triger_object.trigger()
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





