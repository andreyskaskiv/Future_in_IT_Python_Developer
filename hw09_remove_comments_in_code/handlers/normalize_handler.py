import re


def normalize_data_from_file(data: list[str]):
    """Filter data"""
    lines = []

    for line in data:
        line_normalize = re.sub(r'#.*\n$', '\n', line)
        lines.append(line_normalize)

    return lines
