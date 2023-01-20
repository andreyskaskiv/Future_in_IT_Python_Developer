import os
from pathlib import Path
from typing import Callable


from hw07_element_framework_txt.handlers.error_handler import check_file
from hw07_element_framework_txt.handlers.file_handler import read_data_from_file
from hw07_element_framework_txt.handlers.file_handler import filter_data_from_file
from hw07_element_framework_txt.handlers.file_handler import write_data_to_file

from hw07_element_framework_txt.tools.show_table import make_pretty_table
from hw07_element_framework_txt.tools.check_element import check_element

from hw07_element_framework_txt import examples
# print(examples.__file__)
filename = 'elements.txt'  # or pass a function to search for files

PATH_TO_EXAMPLE = os.path.join(Path(examples.__file__).parent, filename)


def main(filename: str, func: Callable):
    """Main controller"""
    if not filename:
        filename = PATH_TO_EXAMPLE

    check = check_file(filename)
    if check:
        return check

    data = read_data_from_file(filename)
    elements_table = filter_data_from_file(data)
    result = func(elements_table)
    return result


def menu():
    """User menu"""
    print('Welcome to txt framework application')
    filename = input('Enter filename or left empty for example: ')
    while True:
        print('Choose menu item: ')
        print("""
                1 - 'Enter element'
                2 - 'Show table elements'
                3 - 'Write data to file'
                0 - 'exit'
                """)
        while True:
            func_name_id = input('Enter number of menu item: ')
            try:
                func_name_id = int(func_name_id)
                break
            except ValueError:
                print('Use only digits')

        if not func_name_id:
            print('Exit from application')
            exit()

        if not 0 < func_name_id <= len(func_map.keys()):
            print('Incorrect menu item')
            continue

        func_keys = list(func_map.keys())
        func_name = func_keys[func_name_id - 1]
        func = func_map[func_name]
        print(f'You have selected this menu item: -{func_name}-')
        print(main(filename, func))
        input('Press enter to continue...')


func_map = {
    'Enter element': check_element,
    'Show table elements': make_pretty_table,
    'Write data to file': write_data_to_file
}


if __name__ == '__main__':
    try:
        menu()
    except (TypeError, ValueError) as error:
        print(error)

