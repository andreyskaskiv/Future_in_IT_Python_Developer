"""Finding the longest word in a file"""
import re
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


def frequency_words(words: list) -> dict:
    """Frequency of the word in the text"""
    frequency_counter = dict(sorted(Counter(words).items(), key=lambda count: count[1], reverse=True))
    return frequency_counter


def sort_len_words(frequency_counter: dict) -> dict:
    """Sort by word length"""
    letter_counter = dict(sorted(frequency_counter.items(), key=lambda word: len(word[0]), reverse=True))
    return letter_counter


def write_data_to_file(frequency_counter: dict, letter_counter: dict, write_file: str):
    """Write statistics into file"""
    with open(write_file, 'w') as file_to_write:
        file_to_write.write('First 10 words in descending order of length.\n\n')
        n = 1
        for word, frequency in letter_counter.items():
            if n <= 10:
                row = f'{n}. word = {word}, len = {len(word)}, frequency = {frequency}\n'
                file_to_write.write(row)
                n += 1
        file_to_write.write('\nThe first 10 words are frequently used.\n\n')
        n = 1
        for word, count in frequency_counter.items():
            if n <= 10:
                row = f'{n}. {word} - {count}\n'
                file_to_write.write(row)
                n += 1


def main(read_file: str, write_file: str = 'romeo_statistic.txt'):
    """Main controller"""
    lines = read_data_from_file(read_file)
    words = filter_data_from_file(lines)
    frequency_counter = frequency_words(words)
    letter_counter = sort_len_words(frequency_counter)
    write_data_to_file(frequency_counter, letter_counter,  write_file)


if __name__ == '__main__':
    main('romeo.txt')
