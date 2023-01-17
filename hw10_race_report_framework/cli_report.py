from typing import Dict

from hw10_race_report_framework.dto.dto import (InfoTable,
                                                DriverCompany)
from hw10_race_report_framework.configurations.menu import menu
from hw10_race_report_framework.handlers.error_handler import check_folder_exist
from hw10_race_report_framework.handlers.report import main as main_report, sort_race_logs
from hw10_race_report_framework.handlers.check_type import check_type
from hw10_race_report_framework.handlers.file_handler import write_data_to_file
from hw10_race_report_framework.tools.show_table import make_pretty_table


def prepare_race_table(race_results: Dict[str, str], abbrs: Dict[str, DriverCompany], current_driver: str, order: str):
    """Prepare race data to console print"""
    race_table = []

    if order == 'asc':
        count = 1
    else:
        count = len(race_results)

    for code in race_results:
        driver = abbrs[code].driver
        company = abbrs[code].company
        race_time = race_results[code]
        counter = count
        if current_driver:
            if driver == current_driver:
                race_table.append(InfoTable(counter, driver, company, race_time))
                break
            continue
        race_table.append(InfoTable(counter, driver, company, race_time))

        if order == 'asc':
            count += 1
        else:
            count -= 1

    if current_driver and not race_table:
        return False
    return race_table


def main(folder: str, final_save: str, final_private: str, output_directory: str, output_filename: str,
         order_asc: bool = True, order_desc: bool = False, driver=''):
    """Main controller of cli_report module"""
    if order_asc and order_desc:
        print('Cannot use two options together: --asc --desc')
        return False

    check_folder_exist(folder)

    race_results, abbrs = main_report(folder)

    order = 'desc' if order_desc else 'asc'
    race_results_sorted = sort_race_logs(race_results, order)
    race_table = prepare_race_table(race_results_sorted, abbrs, driver, order)

    result_table = make_pretty_table(race_table, driver, final_private)

    save_check = check_type(final_save)
    if save_check:
        write_data_to_file(race_table, output_directory, output_filename)

    return result_table


if __name__ == '__main__':
    directory_input, save, private, output_directory, output_filename, order_asc, order_desc, driver = menu()

    try:
        print(main(directory_input, save, private, output_directory, output_filename,
                   order_asc, order_desc, driver))
    except (TypeError, ValueError) as error:
        print(error)
    except FileExistsError as error:
        print(error)
