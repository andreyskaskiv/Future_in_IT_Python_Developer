import os
import re
from pathlib import Path
from typing import List, NamedTuple, Dict

from hw8_baby_names_statistics import baby_names
from hw8_baby_names_statistics.handlers.file_handler import read_data_from_file
from hw8_baby_names_statistics.handlers.file_handler import filter_data_from_file
from hw8_baby_names_statistics.handlers.file_handler import Name


class Filenames(NamedTuple):
    year: int
    sex: str


def split_file(filtered_filenames: List[str]) -> List[Filenames]:
    """Split 1900_BoysNames.txt -> Filenames(year='1900', sex='BoysNames')"""

    names_file_split = []
    for filenames in filtered_filenames:
        match_split = re.split(r"[_\.]", filenames)
        names_file_split.append(Filenames(int(match_split[0]), match_split[1]))

    return names_file_split


def create_template_database(names_file_split: List[Filenames]) -> Dict[int, Dict]:
    """Create a template for the database
    {1900: {'BoysNames': {}, 'GirlsNames': {}}, 1901: {'BoysNames': {}, 'GirlsNames': {}}, ....}"""

    data_base_example = {}
    for filename in names_file_split:
        data_base_example[filename.year] = {file_name.sex: {} for file_name in names_file_split
                                            if file_name.year == filename.year}
    return data_base_example


def get_names_stat(filtered_filename: str) -> List[Name]:
    path_filtered_filename = os.path.join(Path(baby_names.__file__).parent, filtered_filename)
    lines = read_data_from_file(path_filtered_filename)
    names_stat = filter_data_from_file(lines)
    return names_stat


def update_database(template_database: Dict[int, Dict], filtered_filenames: List[str]):
    """Update database"""

    for year, sex in template_database.items():
        for filtered_filename in filtered_filenames:
            if year == int(filtered_filename[:4]):
                if 'BoysNames' in filtered_filename:

                    names_stat = get_names_stat(filtered_filename)
                    for line in names_stat:
                        sex['BoysNames'].setdefault(line.name, line.qty_name)

                elif 'GirlsNames' in filtered_filename:

                    names_stat = get_names_stat(filtered_filename)
                    for line in names_stat:
                        sex['GirlsNames'].setdefault(line.name, line.qty_name)

                else:
                    print('ooops')

    return template_database


def data_base(filtered_filenames: List[str]) -> Dict[int, Dict]:
    """Create a common database"""

    names_file_split = split_file(filtered_filenames)
    template_database = create_template_database(names_file_split)
    data_base_table = update_database(template_database, filtered_filenames)

    return data_base_table

