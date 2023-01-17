from prettytable import PrettyTable
from typing import Any

from prettytable.colortable import ColorTable, Themes


def make_pretty_table(names_count: list[tuple[Any, int]]):
    """Make pretty better result table"""
    result_table = ColorTable(theme=Themes.OCEAN, padding_width=4)
    result_table.field_names = ['Number', 'Name', 'Amount']

    for namber, names_count in enumerate(names_count, 1):
        result_table.add_row([namber, names_count[0], names_count[1]])


    return result_table
