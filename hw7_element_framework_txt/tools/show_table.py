from prettytable import PrettyTable
from hw7_element_framework_txt.handlers.file_handler import Element


def make_pretty_table(elements_table: list[Element]):
    """Make pretty better result table"""
    result_table = PrettyTable()
    result_table.field_names = ['Atomic number', 'Symbol', 'Name']

    for el in elements_table:
        result_table.add_row([el.qty, el.reduction, el.full_name])

    return result_table


