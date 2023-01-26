import unittest
import datetime
from freezegun import freeze_time

from tests_example.time_test.discaunt_calculator import discount_calculator


class TestDiscountCalculator(unittest.TestCase):
    @freeze_time("2022-04-26")
    def test_discount_min_date(self):
        self.assertEqual(
            80.0,
            discount_calculator(
                total_price=100.0,
                due_data=datetime.date(year=2022, month=4, day=28),
                days=3,
                discount=0.2
            )
        )

    @freeze_time("2022-04-28")
    def test_discount_max_date(self):
        self.assertEqual(
            80.0,
            discount_calculator(
                total_price=100.0,
                due_data=datetime.date(year=2022, month=4, day=28),
                days=3,
                discount=0.2
            )
        )

    @freeze_time("2022-04-29")
    def test_discount_over_max_date(self):
        self.assertEqual(
            100.0,
            discount_calculator(
                total_price=100.0,
                due_data=datetime.date(year=2022, month=4, day=28),
                days=3,
                discount=0.2
            )
        )

    @freeze_time("2022-04-25")
    def test_discount_over_min_date(self):
        self.assertEqual(
            100.0,
            discount_calculator(
                total_price=100.0,
                due_data=datetime.date(year=2022, month=4, day=28),
                days=3,
                discount=0.2
            )
        )
