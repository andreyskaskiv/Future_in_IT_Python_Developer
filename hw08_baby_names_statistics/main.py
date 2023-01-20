from typing import Callable

from hw08_baby_names_statistics.handlers.error_handler import check_folder_exist
from hw08_baby_names_statistics.handlers.error_handler import check_files
from hw08_baby_names_statistics.handlers.error_handler import check_input

from hw08_baby_names_statistics.handlers.file_handler import get_filenames_from_folder
from hw08_baby_names_statistics.handlers.file_handler import filter_filenames
from hw08_baby_names_statistics.handlers.file_handler import write_json
from hw08_baby_names_statistics.handlers.file_handler import write_data_to_file

from hw08_baby_names_statistics.handlers.data_base import data_base
from hw08_baby_names_statistics.tools.count_names import count_names
from hw08_baby_names_statistics.tools.show_table import make_pretty_table


PATH_TO_EXAMPLE = 'baby_names'


def run(folder: str, func_name_id: int, func: Callable):
    """Main controller"""
    if not folder:
        folder = PATH_TO_EXAMPLE

    try:
        check_folder_exist(folder)
    except FileExistsError as error:
        return error

    filenames = get_filenames_from_folder(folder)
    filtered_filenames = filter_filenames(filenames)
    check_filenames = check_files(filtered_filenames)

    if check_filenames:
        return check_filenames

    data_base_table = data_base(filtered_filenames)

    if func_name_id == 1:
        info = 'Enter first items table'
        first_items = check_input(info)
        sex_name = 'BoysNames'
        names_count = count_names(data_base_table, sex_name, first_items)
        return make_pretty_table(names_count)

    elif func_name_id == 2:
        info = 'Enter first items table'
        first_items = check_input(info)
        sex_name = 'BoysNames'
        names_count = count_names(data_base_table, sex_name, first_items)
        return write_data_to_file(names_count, sex_name)

    elif func_name_id == 3:
        info = 'Enter first items table'
        first_items = check_input(info)
        sex_name = 'GirlsNames'
        names_count = count_names(data_base_table, sex_name, first_items)
        return make_pretty_table(names_count)

    elif func_name_id == 4:
        info = 'Enter first items table'
        first_items = check_input(info)
        sex_name = 'GirlsNames'
        names_count = count_names(data_base_table, sex_name, first_items)
        return write_data_to_file(names_count, sex_name)

    elif func_name_id == 5:
        json_file_name = input(f'Enter json file name name: ')
        return write_json(data_base_table, json_file_name)


def menu():
    """User menu"""
    print('Welcome to txt framework application')
    path_to_folder = input('Enter path to folder or left empty for example: ')
    while True:
        print('Choose menu item: ')
        print("""
                1 - 'Show table BoysNames'
                2 - 'Write table BoysNames'
                3 - 'Show table GirlsNames'
                4 - 'Write table GirlsNames'
                5 - 'Write database to json'
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
        print(run(path_to_folder, func_name_id, func))
        input('Press enter to continue...')


func_map = {
    'Show table BoysNames': make_pretty_table,
    'Write table BoysNames': write_data_to_file,
    'Show table GirlsNames': make_pretty_table,
    'Write table GirlsNames': write_data_to_file,
    'Write database to file': write_json
}

if __name__ == '__main__':
    try:
        menu()
    except (TypeError, ValueError) as error:
        print(error)
