import time


class Worker:
    normal_sleep_time = 8 * 60 * 60

    def __init__(self, name):
        self.name = name

    def work(self):
        print("Working")
        if self.eat():
            print("Dinner")
        print("Working")

        return 'Work is done'

    def eat(self):
        time.sleep(30 * 60)
        result1 = self.food(1)
        result2 = self.food(2)
        result3 = self.food(3)

        return result1 + result2 + result3

    def sleep(self, sleep_time):
        if sleep_time > 12 * 60 * 60:
            self.wake_up()

    def wake_up(self):
        raise Exception('Wake up')

    def can_repeat(self, sleep_time):
        if sleep_time >= self.normal_sleep_time:
            result = True
        else:
            result = False

        return result


