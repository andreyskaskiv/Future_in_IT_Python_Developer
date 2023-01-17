from typing import List
from prettytable.colortable import ColorTable, Themes

from hw10_race_report_framework.dto.dto import InfoTable
from hw10_race_report_framework.handlers.check_type import check_type


def make_pretty_table(race_table: List[InfoTable], driver: str, private: str):
    """Make pretty better result table"""
    # # Color
    # R = "\033[0;31;40m"  # RED
    # G = "\033[0;32;40m"  # GREEN
    # Y = "\033[0;33;40m"  # Yellow
    # B = "\033[0;34;40m"  # Blue
    # N = "\033[0m"  # Reset

    result_table = ColorTable(theme=Themes.OCEAN, padding_width=2)
    result_table.field_names = ['№', 'Driver', 'Company', 'Race time']
    result_table.align['Driver'] = "l"
    result_table.align['Company'] = "l"

    if not race_table:

        return False
    for info_table in race_table:
        color = "\033[1;32m%s\033[0m" if info_table.counter <= 15 else "\033[1;31m%s\033[0m"

        counter = color % info_table.counter
        driver = color % info_table.driver
        company = color % info_table.company
        race_time = color % info_table.race_time

        private_check = check_type(private)

        if private_check and info_table.counter <= 3:
            driver_name = '*' * len(driver)
        else:
            driver_name = driver

        result_table.add_row([counter, driver_name, company, race_time])

        if info_table.counter == 15:
            result_table.add_row(['-'*len(counter[:4]), '-'*len(driver_name), '-'*len(company), '-'*len(race_time[:15])])

    return result_table




