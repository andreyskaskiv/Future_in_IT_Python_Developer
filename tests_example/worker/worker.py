import time


class Worker:
    normal_sleep_time = 8 * 60 * 60

    def __init__(self, name):
        self.name = name

    def work(self):
        pass

    def eat(self):
        pass

    def sleep(self, sleep_time):
        pass

    def wake_up(self):
        pass

    def can_repeat(self, sleep_time):
        pass
