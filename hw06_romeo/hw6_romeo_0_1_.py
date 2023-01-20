"""Finding the longest word in a file"""
import re
from collections import namedtuple
from typing import List, NamedTuple
from collections import Counter


def read_data_from_file(read_file: str) -> str:
    """Read data from file"""
    with open(read_file) as file:
        words = str(file.readlines()).lower()
    return words


def filter_data_from_file(lines: str):
    """Filter only words"""
    # match_words = re.compile(r'[a-zA-Z\-]{3,}')
    match_words = re.compile(r'[a-zA-Z]{3,}')
    words = match_words.findall(lines)
    return words


def sort_len_words(words: list[str]) -> list[str]:
    """Sort by word length"""
    sorted_words = sorted(set(words), key=len, reverse=True)
    return sorted_words


def frequency_words(words: list[str]) -> dict[str | int]:
    """Frequency of the word in the text"""
    counter = dict(Counter(words))
    return counter


def write_data_to_file(sorted_words: list[str], counter: dict[str | int], write_file: str):
    """Write statistics into file"""
    for word in sorted_words:
        print(word, counter[word])


    # with open(write_file, 'w') as file_to_write:
    #     for count_line, line in enumerate(names_stat, 1):
    #         row = f'{count_line}|{line.name}|{line.qty_name}\n'
    #         file_to_write.write(row)


def main(read_file: str, write_file: str = 'romeo_statistic.txt'):
    """Main controller"""
    lines = read_data_from_file(read_file)
    words = filter_data_from_file(lines)

    sorted_words = sort_len_words(words)
    # print(sorted_words)

    counter = frequency_words(words)
    # print(counter)

    write_data_to_file(sorted_words, counter,  write_file)


if __name__ == '__main__':
    main('romeo.txt')
