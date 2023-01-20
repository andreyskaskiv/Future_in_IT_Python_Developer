import os
from pathlib import Path
from typing import List

from hw08_baby_names_statistics import baby_names


def check_folder_exist(folder: str):
    """Check folder exist"""
    if not os.path.exists(folder):
        raise FileExistsError(f'Folder {folder} not exist')


def check_files(filtered_filenames: List[str]):
    """Check exist file and txt format"""
    for filtered_filename in filtered_filenames:
        path_filtered_filename = os.path.join(Path(baby_names.__file__).parent, filtered_filename)

        try:
            with open(path_filtered_filename, mode='rt') as file:
                file.read()
        except FileNotFoundError as error:
            return error
        except UnicodeDecodeError:
            return 'Application works only with txt files.'


def check_input(info: str):
    """Check user input for a number"""
    while True:
        element = input(f'{info}: ')
        try:
            element = int(element)
            return element
        except ValueError:
            print('Use only digits')