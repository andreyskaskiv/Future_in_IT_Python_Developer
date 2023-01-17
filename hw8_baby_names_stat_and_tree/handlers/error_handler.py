import os
from pathlib import Path
from typing import List, NamedTuple

from hw8_baby_names_stat_and_tree import baby_names
from hw8_baby_names_stat_and_tree.DTO.DTO import Identification
from hw8_baby_names_stat_and_tree.client.id import CLIENTS


def check_identification(client: Identification[NamedTuple]):
    for clients in CLIENTS:
        for id_client in CLIENTS[clients]:
            if clients in client.username:
                if id_client.password not in client.password:
                    print(f'Enter username {client.username} or password {client.password} does not match.')
                    exit()


def check_folder_exist(folder: str):
    """Check folder exist"""
    if not os.path.exists(folder):
        raise FileExistsError(f'Folder {folder} not exist')

    if not os.path.isdir(folder):
        raise TypeError(f'{folder} is not a folder')


def check_file_exist(filename: str):
    """Check if file exist"""
    if not os.path.exists(filename):
        return False

    if not os.path.isfile(filename):
        return False
    return True


def check_file_type_txt(filename: str):
    """Check if txt file format"""
    try:
        open(filename).read()
    except UnicodeDecodeError:
        return False
    return True


# def check_files(filtered_filenames: List[str]):
#     """Check exist file and txt format"""
#     for filtered_filename in filtered_filenames:
#         path_filtered_filename = os.path.join(Path(baby_names.__file__).parent, filtered_filename)
#
#         try:
#             with open(path_filtered_filename, mode='rt') as file:
#                 file.read()
#         except UnicodeDecodeError:
#             return 'Application works only with txt files.'
