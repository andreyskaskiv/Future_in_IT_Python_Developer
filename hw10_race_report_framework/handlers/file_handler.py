import os
from typing import List

from hw10_race_report_framework.handlers.error_handler import check_file_type

from hw10_race_report_framework.dto.dto import InfoTable


def read_data_from_file(filename: str):
    """Read data from race files"""

    if not check_file_type(filename):
        return False

    data = []
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if line:
                data.append(line)
    return data


def write_data_to_file(race_table: List[InfoTable], output_directory: str, output_filename: str):
    file_output = os.path.join(output_directory, output_filename)
    """Write names statistics into file"""
    with open(file_output, 'w') as file_to_write:
        for line in race_table:
            row = f'{line.counter} {line.driver} {line.company} {line.race_time}\n'
            file_to_write.write(row)

    print(f'path to file --> {file_output}')
    return f'File name "{output_filename}"'