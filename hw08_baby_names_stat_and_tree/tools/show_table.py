from distutils.util import strtobool
from typing import Any, List
from prettytable.colortable import ColorTable, Themes


def make_pretty_table(names_count: list[tuple[Any, int]], show_all_names: str, ban_names: List[str]):
    """Make pretty better result table"""
    result_table = ColorTable(theme=Themes.OCEAN, padding_width=4)
    result_table.field_names = ['Number', 'Name', 'Amount']

    for number, name_count in enumerate(names_count, 1):
        if not strtobool(show_all_names):
            name = '*' * len(name_count[0]) if name_count[0] in ban_names else name_count[0]
        else:
            name = name_count[0]

        result_table.add_row([number, name, name_count[1]])

    return result_table
