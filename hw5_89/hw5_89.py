"""Search for magic numbers"""
from typing import Any


def check_length_input(*args: Any):
    """Сheck input counts"""
    if len(args) != 2:
        raise TypeError('Enter two integers')


def check_date_type(*args: Any):
    """Check data type"""
    len_numbers = len([number for number in args if isinstance(number, int)])
    if len_numbers != len(args):
        raise TypeError('Input only interger')


def separation_digit(number: int) -> int:
    """Split into components"""
    components = []
    counter = len(str(number))
    while number != 0:
        components.append((number % 10) ** counter)
        number = number // 10
        counter -= 1
    return sum(components)


def take_out_numbers(*args: int) -> list[int]:
    """Filter by specified conditions"""
    start, stop = args
    return [num for num in range(start, stop + 1) if num == separation_digit(num)]


def main(*args: int) -> list[int]:
    """Main controller"""
    check_length_input(*args)
    check_date_type(*args)
    result = take_out_numbers(*args)
    return result


def check_test():
    """Check input and return"""
    result = main(90, 100)
    assert result == [], f'Wrong answer: {result}'

    result = main(1, 10)
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9], f'Wrong answer: {result}'

    result = main(1, 100)
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 89], f'Wrong answer: {result}'

    result = main(1, 1000)
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 89, 135, 175, 518, 598], f'Wrong answer: {result}'

    result = main(10, 1000)
    assert result == [89, 135, 175, 518, 598], f'Wrong answer: {result}'

    result = main(1, 900000)
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 89, 135, 175, 518, 598, 1306, 1676, 2427], f'Wrong answer: {result}'

    print('All assert_tests passed!')


if __name__ == '__main__':
    check_test()

    # try:
    #     print(main(1, 'efwg'))
    # except (TypeError, ValueError) as error:
    #     print(error)





