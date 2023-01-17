"""Написать функцию проверки «силы» пароля, возвращает всегда строку
- если пароль короче 8 символов, то вернуть Too Weak
- если пароль содержит только цифру, только строчные, только заглавные, то вернуть Weak
- если пароль содержит символы любых 2 наборов вернуть Good
- если пароль содержит символы любый 3 наборов, вернуть Very Good
"""

import string
from collections import namedtuple


def password_strength(value: str) -> str:
    DIGITS = string.digits
    LOWERS = string.ascii_lowercase
    UPPERS = LOWERS.upper()

    if len(value) < 8:
        return 'Too Weak'

    COUNT = 0
    for symbols in (DIGITS, LOWERS, UPPERS):
        if any(symbol in symbols for symbol in value):
            COUNT += 1
            continue  # обязательно, для перехода к другому набору

    if COUNT == 3:
        return 'Very Good'
    return 'Weak' if COUNT == 1 else 'Good'


if __name__ == '__main__':
    # safety net
    Case = namedtuple('Case', 'password answer')

    CASES = (
        Case('', 'Too Weak'),
        Case('1234567', 'Too Weak'),
        Case('qwertyu', 'Too Weak'),
        Case('QWERTYU', 'Too Weak'),
        Case('qwQW133', 'Too Weak'),

        Case('12345678', 'Weak'),
        Case('123456789', 'Weak'),
        Case('qwertyui', 'Weak'),
        Case('qwertyuiv', 'Weak'),
        Case('QWERTYUI', 'Weak'),
        Case('QWERTYUIW', 'Weak'),

        Case('1234qwer', 'Good'),
        Case('1234qwer5', 'Good'),
        Case('1234QWER', 'Good'),
        Case('1234QWERS', 'Good'),
        Case('QWERqwer', 'Good'),
        Case('1234qwer', 'Good'),
        Case('QWERqwerw', 'Good'),

        Case('123qweQWE', 'Very Good'),
        Case('123qLLQWE', 'Very Good'),
        Case('123456Waw', 'Very Good'),
    )

    for case in CASES:
        assert password_strength(case.password) == case.answer


