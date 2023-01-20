from distutils.util import strtobool
import json
import os
import re
from typing import List,  Dict, Any

from hw08_baby_names_stat_and_tree.DTO.DTO import Name
from hw08_baby_names_stat_and_tree.handlers.error_handler import (check_file_exist,
                                                                  check_file_type_txt)


def get_filenames_from_folder(folder: str):
    """Get list of filenames in folder"""
    filenames = os.listdir(folder)
    return filenames


def filter_filenames(filenames: List[str], filename_filter: str) -> List[str]:
    """Check filenames format 1900_BoysNames.txt"""
    match_filename = re.compile(filename_filter)
    filtered_filenames = []
    for filename in filenames:
        if match_filename.search(filename):
            filtered_filenames.append(filename)

    return filtered_filenames


def read_data_from_file(read_file: str):
    """Read data from file"""
    if not check_file_exist(read_file):
        return False

    if not check_file_type_txt(read_file):
        return False

    lines = []
    with open(read_file) as file:
        for line in file:
            line = line.strip()
            if line:
                lines.append(line)

    return lines


def filter_data_from_file(lines: List[str]) -> List[Name]:
    """Filter name and qty names from file"""
    names_stat = []
    match_name = re.compile(r'[a-zA-Z]+')
    match_qty_name = re.compile(r'[0-9]+')
    for line in lines:
        name = match_name.search(line)
        qty_name = match_qty_name.search(line)
        if name.group() and qty_name.group():
            name = name.group().capitalize()
            qty_name = int(qty_name.group())
            names_stat.append(
                Name(name, qty_name))

    return names_stat


def write_json(data_base_table: Dict[int, Dict], json_file_name: str = 'baby_names_statistics_end_ex_fo_teacher'):
    """Write dict object to json"""
    with open(json_file_name + '.json', 'w') as file:
        json.dump(data_base_table, file, indent=4)

    return f'File name "{json_file_name}.json"'


def write_data_to_file(names_stat: list[tuple[Any, int]], write_file: str, show_all_names: str, ban_names: List[str]):
    """Write names statistics into file"""
    with open(write_file + '.txt', 'w') as file_to_write:
        for count_line, line in enumerate(names_stat, 1):

            if not strtobool(show_all_names):
                name = '*' * len(line[0]) if line[0] in ban_names else line[0]
            else:
                name = line[0]

            row = f'{count_line}|{name}|{line[1]}\n'
            file_to_write.write(row)

    return f'File name "{write_file}.txt"'


def write_tree_to_file(tree: list[str], write_file: str = 'directory_tree.txt'):
    """Write tree to file"""
    with open(write_file, 'w') as file_to_write:
        for line in tree:
            file_to_write.write(line)

    return f'File name "{write_file}"'
