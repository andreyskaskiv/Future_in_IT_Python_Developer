import re
from collections import namedtuple
from typing import List, NamedTuple


class Element(NamedTuple):
    qty: int
    reduction: str
    full_name: str


def read_data_from_file(read_file: str) -> list[str]:
    """Read data from file"""
    lines = []
    with open(read_file) as file:
        for line in file:
            line = line.strip()
            if line:
                lines.append(line)

    return lines


def check_data_type(qty: str, reduction: str, full_name: str):
    """Check data type"""
    if not qty.isdigit():
        raise TypeError(f'Invalid qty data type {type(qty)}')

    if not isinstance(reduction, str):
        raise TypeError(f'Invalid reduction data type {type(reduction)}')

    if not isinstance(full_name, str):
        raise TypeError(f'Invalid full_name data type {type(full_name)}')


def filter_data_from_file(data: list[str]) -> list[Element]:
    """Filter data and check"""
    elements_table = []

    for line in data:
        if len(re.split(r"[ .':;,\"|]+", line)) != 3:
            raise ValueError(f'len "{line}" != 3')

        qty, reduction, full_name = re.split(r"[ .':;,\"|]+", line)
        check_data_type(qty, reduction, full_name)

        qty = int(qty)
        reduction = reduction.capitalize()
        full_name = full_name.capitalize()

        elements_table.append(
            Element(qty, reduction, full_name))

    return elements_table


def write_data_to_file(elements_table: list[Element]):
    """Write elements into file"""
    write_file = input(f'Enter file name: ')
    with open(write_file + '.txt', 'w') as file_to_write:
        for line in elements_table:
            row = f'{line.qty}|{line.reduction}|{line.full_name}\n'
            file_to_write.write(row)

    return write_file
