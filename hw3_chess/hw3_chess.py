from prettytable import PrettyTable

chess_letter = 'abcdefgh'

chess_board: list[list[int]] = [[(0 if lines % 2 == 0 else 1) if columns % 2 == 0 else (1 if lines % 2 == 0 else 0)
                                 for lines in range(8)] for columns in range(8)]


def input_validation(func):
    def wrapper(*args):
        args = str(*args)
        if len(args) >= 3 or len(args) <= 1:
            return 'You must enter two characters, for example "a1".'

        input_letter, input_number = args[0], args[1]
        if (input_letter not in chess_letter) or (input_number not in '12345678'):
            return 'You entered incorrect values. Letter must be in the range "abcdefgh" and Number in the range ' \
                   '"12345678" '

        input_number = int(input_number)
        result = func(input_letter, input_number)
        return result

    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__

    return wrapper


@input_validation
def definition_color(input_letter: str, input_number: int):
    """
    We get coordinates as input.
    :return: Based on the received coordinates, we get the color of the cell.
    """

    for _ in chess_letter:
        if ((input_letter in chess_letter[::2] and input_number % 2 != 0) or
                (input_letter in chess_letter[1::2] and input_number % 2 == 0)):
            return 'White'
        else:
            return 'Black'


if __name__ == '__main__':
    input_user = input('Enter coordinates: ')
    print(f'input_user = {input_user},  cell_color = {definition_color(input_user)}', end='\n' * 3)

    print(f'Use next values:')
    cli_table = PrettyTable()
    cli_table.field_names = [*chess_letter]
    for num in сhess_board:
        cli_table.add_row([*num])

    print(cli_table)
