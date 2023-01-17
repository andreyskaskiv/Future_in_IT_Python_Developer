from unittest import TestCase, main

from hw15_Tk_unittest_calc.hw15_Calc_Tk_unittest import calc
from tests_example.unit_tests.calc_1 import calculator

# red-green refactoring

class CalculatorTest(TestCase):
    # Positive tests
    def test_plus(self):
        self.assertEqual(calculator('2+2'), 4)

    def test_minus(self):
        self.assertEqual(calculator('3-1'), 2)

    def test_multi(self):
        self.assertEqual(calculator('4*4'), 16)

    def test_divide(self):
        self.assertEqual(calculator('10/5'), 2.0)

    # Negative tastes
    def test_no_signs(self):
        with self.assertRaises(ValueError) as error:
            calculator('asasasas')
        self.assertEqual("Выражение должно содержать хотя бы один знак '(+-/*)'",
                         error.exception.args[0])  # args[0] проверка текста исключения

    def test_two_signs(self):
        with self.assertRaises(ValueError) as error:
            calculator('2+2+2')
        self.assertEqual("Выражение должно содержать 2 целых числа и 1 знак",
                         error.exception.args[0])  # args[0] проверка текста исключения

    def test_many_signs(self):
        with self.assertRaises(ValueError) as error:
            calculator('2+3*10')
        self.assertEqual("Выражение должно содержать 2 целых числа и 1 знак",
                         error.exception.args[0])  # args[0] проверка текста исключения

    def test_no_ints(self):
        with self.assertRaises(ValueError) as error:
            calculator('2.3+5.6')
        self.assertEqual("Выражение должно содержать 2 целых числа и 1 знак",
                         error.exception.args[0])  # args[0] проверка текста исключения

    def test_strings(self):
        with self.assertRaises(ValueError) as error:
            calculator('a+b')
        self.assertEqual("Выражение должно содержать 2 целых числа и 1 знак",
                         error.exception.args[0])  # args[0] проверка текста исключения


if __name__ == '__main__':
    main()
