import json
import os
import re
from typing import List, NamedTuple, Dict, Any


def get_filenames_from_folder(folder: str):
    """Get list of filenames in folder"""
    filenames = os.listdir(folder)
    return filenames


def filter_filenames(filenames: List[str]) -> List[str]:
    """Check filenames format 1900_BoysNames.txt"""
    match_filename = re.compile(r'^[1-2][09][0-9][0-9]_(BoysNames|GirlsNames)\.txt$')
    filtered_filenames = []
    for filename in filenames:
        if match_filename.search(filename):
            filtered_filenames.append(filename)

    return filtered_filenames


class Name(NamedTuple):
    name: str
    qty_name: int


def read_data_from_file(read_file: str) -> List[str]:
    """Read data from file"""
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


def write_json(data_base_table: Dict[int, Dict], json_file_name: str):
    """Write dict object to json"""
    with open(json_file_name + '.json', 'w') as file:
        json.dump(data_base_table, file, indent=4)

    return f'File name "{json_file_name}.json"'


def write_data_to_file(names_stat: list[tuple[Any, int]], write_file: str):
    """Write names statistics into file"""
    with open(write_file + '.txt', 'w') as file_to_write:
        for count_line, line in enumerate(names_stat, 1):
            row = f'{count_line}|{line[0]}|{line[1]}\n'
            file_to_write.write(row)

    return f'File name "{write_file}.txt"'
