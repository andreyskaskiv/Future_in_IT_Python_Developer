"""Написать функцию проверки «силы» пароля, возвращает всегда строку
- если пароль короче 8 символов, то вернуть Too Weak
- если пароль содержит только цифру, только строчные, только заглавные, то вернуть Weak
- если пароль содержит символы любых 2 наборов вернуть Good
- если пароль содержит символы любый 3 наборов, вернуть Very Good
"""
import string


def password_strength(value: str) -> str:
    DIGITS = string.digits
    LOWERS = string.ascii_lowercase
    UPPERS = LOWERS.upper()

    if len(value) < 8:
        return 'Too Weak'
    if all(symbol in DIGITS for symbol in value) or \
            all(symbol in LOWERS for symbol in value) or \
            all(symbol in UPPERS for symbol in value):
        return 'Weak'
    if any(symbol in DIGITS for symbol in value) and \
            any(symbol in LOWERS for symbol in value) and \
            any(symbol in UPPERS for symbol in value):
        return 'Very Good'
    if (any(symbol in DIGITS for symbol in value) and any(symbol in LOWERS for symbol in value)) or \
            (any(symbol in DIGITS for symbol in value) and any(symbol in UPPERS for symbol in value)) or \
            (any(symbol in LOWERS for symbol in value) and any(symbol in UPPERS for symbol in value)):
        return 'Good'


if __name__ == '__main__':
    # safety net
    assert password_strength('') == 'Too Weak'
    assert password_strength('1234567') == 'Too Weak'
    assert password_strength('qwertyu') == 'Too Weak'
    assert password_strength('QWERTYU') == 'Too Weak'
    assert password_strength('qwQW133') == 'Too Weak'

    assert password_strength('12345678') == 'Weak'
    assert password_strength('123456789') == 'Weak'
    assert password_strength('qwertyui') == 'Weak'
    assert password_strength('qwertyuiv') == 'Weak'
    assert password_strength('QWERTYUI') == 'Weak'
    assert password_strength('QWERTYUIW') == 'Weak'

    assert password_strength('1234qwer') == 'Good'
    assert password_strength('1234qwer5') == 'Good'
    assert password_strength('1234QWER') == 'Good'
    assert password_strength('1234QWERS') == 'Good'
    assert password_strength('QWERqwer') == 'Good'
    assert password_strength('QWERqwerw') == 'Good'

    assert password_strength('123qweQWE') == 'Very Good'
    assert password_strength('123qLLQWE') == 'Very Good'
    assert password_strength('123456Waw') == 'Very Good'
