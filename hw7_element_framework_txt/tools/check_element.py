import re

from hw7_element_framework_txt.handlers.file_handler import Element
from hw7_element_framework_txt.tools.show_table import make_pretty_table


def check_user_input(user_input: str, elements_table: list[Element]):
    """Check user_input"""
    if user_input.isdigit():
        user_input = int(user_input)
    else:
        user_input = user_input.capitalize()

    variable = user_input

    if not re.findall(r'\b' + str(variable) + r'\b', str(elements_table)):
        print(make_pretty_table(elements_table))
        raise ValueError(f'Enter element {user_input} not find.')

    return user_input


def check_element(elements_table: list[Element]):
    """Check input of table"""
    user_input = input('Enter element symbol or number of atoms: ')
    user_input = check_user_input(user_input, elements_table)

    for element in elements_table:
        if user_input in element:
            print('*  ' * 8)
            return f'  Atomic number = {element.qty},\n' \
                   f'  Symbol = {element.reduction},\n' \
                   f'  Name = {element.full_name} \n'






