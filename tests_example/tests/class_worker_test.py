import unittest
from unittest.mock import patch

from tests_example.worker import worker


class TestWorker(unittest.TestCase):
    def test_can_repeat(self):
        pass

    def test_sleep(self):
        pass

    def test_work(self):
        pass

    @patch.object(worker.Worker, 'eat')
    def test_work_1(self, mock_eat):
        pass

    @staticmethod
    def food_se(self):
        pass

    @patch('worker.time.sleep')
    def test_eat(self, mock_time_sleep):
        pass


if __name__ == '__main__':
    unittest.main()
