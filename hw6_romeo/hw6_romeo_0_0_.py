"""Finding the longest word in a file"""
import re
from collections import namedtuple
from typing import List, NamedTuple
from collections import Counter


def read_data_from_file(read_file: str) -> str:
    """Read data from file"""
    lines = []
    with open(read_file) as file:
        for line in file:
            line = line.strip() #  возвращает копию строки, удаляя как начальные, так и конечные символы
            if line:
                lines.append(line.lower())
    return str(lines)


def filter_data_from_file(lines: str):
    """Filter only words"""
    # match_words = re.compile(r'[a-zA-Z\-]{3,}')
    match_words = re.compile(r'[a-zA-Z]{3,}')
    words = match_words.findall(lines)
    return words


def count_len_words(words: list[str]):
    return sorted(words, key=len, reverse=True)


def counter_words(sorted_words: list[str]):
    counter = Counter(sorted_words)
    return counter


# def write_data_to_file(names_stat: List[Name], write_file: str):
#     """Write names statistics into file"""
#     with open(write_file, 'w') as file_to_write:
#         for count_line, line in enumerate(names_stat, 1):
#             row = f'{count_line}|{line.name}|{line.qty_name}\n'
#             file_to_write.write(row)


def main(read_file: str, write_file: str = 'example.txt'):
    """Main controller"""
    lines = read_data_from_file(read_file)
    words = filter_data_from_file(lines)

    sorted_words = count_len_words(words)
    print(sorted_words)

    # counter = counter_words(sorted_words)
    # print(counter)

    # write_data_to_file(names_stat, write_file)


if __name__ == '__main__':
    main('romeo.txt')

