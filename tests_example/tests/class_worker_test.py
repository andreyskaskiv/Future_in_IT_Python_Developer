import unittest
from unittest.mock import patch, Mock

from tests_example.worker import worker


class TestWorker(unittest.TestCase):

    # def test_can_repeat(self):  # checks out ONLY ONE branch
    #     sleep_time = 7 * 60 * 60
    #     expected_result = False
    #
    #     new_worker = worker.Worker('Bob')
    #     result = new_worker.can_repeat(sleep_time)
    #
    #     self.assertEqual(expected_result, result)

    def test_can_repeat_cases(self):  # go to each branch of the condition
        test_cases = [
            {
                'arguments': {'sleep_time': 9 * 60 * 60},
                'expected_result': True
            },
            {
                'arguments': {'sleep_time': 7 * 60 * 60},
                'expected_result': False
            }
        ]

        new_worker = worker.Worker('Alice')
        for test_case in test_cases:
            # result = new_worker.can_repeat(sleep_time=9*60*60)
            result = new_worker.can_repeat(**test_case['arguments'])

            self.assertEqual(test_case['expected_result'], result)

    def test_sleep(self):
        sleep_time = 13 * 60 * 60
        new_worker = worker.Worker('Bob')

        with self.assertRaises(Exception):
            _ = new_worker.sleep(sleep_time)

    def test_work(self):
        pass

    @patch.object(worker.Worker, 'eat')  # class Worker, change the method 'eat'
    def test_work_1(self, mock_eat):  # eat == mock_eat
        mock_eat.return_value = True  # and change the return value to True

        new_worker = worker.Worker('Bob')

        result = new_worker.work()

        self.assertEqual('Work is done', result)
        mock_eat.assert_called()  # called once
        # mock_eat.assert_not_called()  # checking whether the caller was called or not

    @staticmethod
    def food_se(args):  # args == 1, 2, 3 with func eat, "result1 = self.food(1) ...."
        food_dict = {
            1: 'apple',
            2: 'bread',
            3: 'cheese'
        }

        return food_dict.get(args)

    @patch('worker.time.sleep')  # to replace the function sleep, do 'worker.time.sleep'
    def test_eat(self, _):  # time_sleep == mock_time_sleep == _
        new_worker = worker.Worker('Rock')

        new_worker.food = Mock(side_effect=self.food_se)

        result = new_worker.eat()

        self.assertEqual('applebreadcheese', result)


if __name__ == '__main__':
    unittest.main()
