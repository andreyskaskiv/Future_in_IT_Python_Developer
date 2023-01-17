"""A program to remove comment lines from a file in Python."""

from hw9_remove_comments_in_code.handlers.error_handlers import check_file
from hw9_remove_comments_in_code.handlers.normalize_handler import normalize_data_from_file
from hw9_remove_comments_in_code.handlers.file_handlers import (read_data_from_file,
                                                                write_data_to_file)


def main(filename: str, write_file: str = 'data/output_normalize_data.py'):
    """Main controller"""
    check = check_file(filename)
    if check:
        return check

    data = read_data_from_file(filename)
    normalize_data = normalize_data_from_file(data)
    write_data_to_file(normalize_data, write_file)


if __name__ == '__main__':
    file_name = 'data/test_big.py'

    try:
        main(file_name)
    except (TypeError, ValueError) as error:
        print(error)
