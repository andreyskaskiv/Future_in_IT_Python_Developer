"""Написать функцию калькулятор, которая принимает на вход строку,
содержащую два целых числа и один знак арифметической  операции +-/* и
возвращает результат выполнения этой операции.
Если числа не целые или нет знака операции, то бросать исключение ValueError"""

"""
Порядок действий:
1) создаем папку tests_example (не пакет!)
2) создаем модуль в стиле функция_test.py
3) сначала пишем позитивные тесты (те, где все хорошо)
4) тест должен быть сначала красный, проверяем что он проверяет что нужно
5) не забываем покрывать тестами ветки условий и исключений
6) после каждого действия или изменения запускаем тесты
7) создаем конфигурацию запуска всех тестов
8) используем покрытие кода (code coverage) как информацию о том, что не покрыто тестами
9) при рефакторинге постоянно запускаем тесты

https://docs.python.org/3/library/unittest.html?highlight=unittest#module-unittest
"""


def calculator(expression):
    allowed = '+-/*'
    if not any(sign in expression for sign in allowed):
        raise ValueError(f"Выражение должно содержать хотя бы один знак '({allowed})'")
    for sign in allowed:
        if sign in expression:
            try:
                left, right = expression.split(sign)  # ValueError
                left, right = int(left), int(right)  # TypeError
                if sign == '+':
                    return left + right
                elif sign == '-':
                    return left - right
                elif sign == '*':
                    return left * right
                elif sign == '/':
                    return left / right
            except (ValueError, TypeError):
                raise ValueError("Выражение должно содержать 2 целых числа и 1 знак")


if __name__ == '__main__':
    print(calculator('10/2'))
