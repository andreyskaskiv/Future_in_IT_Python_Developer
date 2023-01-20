from hw08_baby_names_stat_and_tree.handlers.data_base import data_base
from hw08_baby_names_stat_and_tree.handlers.config_handlers import Config
from hw08_baby_names_stat_and_tree.tools.count_names import count_names
from hw08_baby_names_stat_and_tree.tools.show_table import make_pretty_table
from hw08_baby_names_stat_and_tree.DTO.DTO import Args
from hw08_baby_names_stat_and_tree.tools.generate_tree import generate_tree
from hw08_baby_names_stat_and_tree.handlers.error_handler import (check_folder_exist,
                                                                  check_identification)
from hw08_baby_names_stat_and_tree.handlers.file_handler import (filter_filenames,
                                                                 get_filenames_from_folder,
                                                                 write_data_to_file,
                                                                 write_json,
                                                                 write_tree_to_file)

conf = Config()
PATH_TO_FOLDER = conf.get_path_to_folder()
client = conf.identification()
BABY_NAMES_FILTER = conf.get_names_filter_file()


def run(folder: str, func: Args):
    """Main controller"""

    check_identification(client)
    check_folder_exist(folder)

    filenames = get_filenames_from_folder(folder)
    filtered_filenames = filter_filenames(filenames, BABY_NAMES_FILTER)
    data_base_table = data_base(filtered_filenames)
    names_count = count_names(data_base_table, func.gender, func.quantity)
    directory_tree = generate_tree('.')

    if func.function == make_pretty_table:
        return func.function(names_count, func.show_all_names, conf.banned())

    elif func.function == write_data_to_file:
        return func.function(names_count, func.gender, func.show_all_names, conf.banned())

    elif func.function == write_json:
        return func.function(data_base_table)

    elif func.function == write_tree_to_file:
        return func.function(directory_tree)

    else:
        print('Once more...')


def menu():
    """User menu"""
    print('Welcome to txt framework application')
    path_to_folder = PATH_TO_FOLDER
    while True:
        print('Choose menu item: ')
        print("""
                1 - 'Show table BoysNames'
                2 - 'Write table BoysNames'
                3 - 'Show table GirlsNames'
                4 - 'Write table GirlsNames'
                5 - 'Write database to json'
                6 - 'Write directory tree'
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

        if not 0 < func_name_id <= len(func_map_attribute.keys()):
            print('Incorrect menu item')
            continue

        func_keys = list(func_map_attribute.keys())
        func_name = func_keys[func_name_id - 1]
        func = func_map_attribute[func_name]
        print(f'You have selected this menu item: -{func_name}-')
        print(run(path_to_folder, func))
        input('Press enter to continue...')


func_map_attribute = {
    'Show table BoysNames': Args(make_pretty_table,
                                 conf.get_gender().Boys,
                                 int(conf.get_quantity()),
                                 conf.show_all_names()),
    'Write table BoysNames': Args(write_data_to_file,
                                  conf.get_gender().Boys,
                                  int(conf.get_quantity()),
                                  conf.show_all_names()),
    'Show table GirlsNames': Args(make_pretty_table,
                                  conf.get_gender().Girls,
                                  int(conf.get_quantity()),
                                  conf.show_all_names()),
    'Write table GirlsNames': Args(write_data_to_file,
                                   conf.get_gender().Girls,
                                   int(conf.get_quantity()),
                                   conf.show_all_names()),
    'Write database to file': Args(write_json,
                                   conf.get_gender().Boys,
                                   int(conf.get_quantity()),
                                   conf.show_all_names()),
    'Write directory tree': Args(write_tree_to_file,
                                 conf.get_gender().Boys,
                                 int(conf.get_quantity()),
                                 conf.show_all_names())
}

if __name__ == '__main__':
    try:
        menu()
    except (TypeError, ValueError) as error:
        print(error)
    except FileExistsError as error:
        print(error)
