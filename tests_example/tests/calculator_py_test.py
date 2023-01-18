import pytest

from tests_example.calculator.calc_1 import calculator


# red-green refactoring


# Positive tests
def test_plus():
    assert calculator('2+2') == 4


def test_minus():
    assert calculator('3-1') == 2


def test_multi():
    assert calculator('4*4') == 16


def test_divide():
    assert calculator('10/5') == 2.0


# Negative tastes
def test_no_signs():
    with pytest.raises(ValueError) as error:
        calculator('asasasas')
    assert "Выражение должно содержать хотя бы один знак '(+-/*)'" == error.value.args[0]


def test_two_signs():
    with pytest.raises(ValueError) as error:
        calculator('2+2+2')
    assert "Выражение должно содержать 2 целых числа и 1 знак" == error.value.args[0]


def test_many_signs():
    with pytest.raises(ValueError) as error:
        calculator('2+3*10')
    assert "Выражение должно содержать 2 целых числа и 1 знак" == error.value.args[0]


def test_no_ints():  # args[0] проверка текста исключения
    with pytest.raises(ValueError) as error:
        calculator('2.3+5.6')
    assert "Выражение должно содержать 2 целых числа и 1 знак" == error.value.args[0]


def test_strings():
    with pytest.raises(ValueError) as error:
        calculator('a+b')
    assert "Выражение должно содержать 2 целых числа и 1 знак" == error.value.args[0]


if __name__ == '__main__':
    pytest.main()
