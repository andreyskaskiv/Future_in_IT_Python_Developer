def read_data_from_file(read_file: str) -> list[str]:
    with open(read_file) as file:
        lines = []
        for line in file:
            if line.startswith('#'):
                continue
            lines.append(line)
    return lines


def write_data_to_file(data, write_file: str):
    """Write data to a file"""
    with open(write_file, 'w') as file_to_write:
        file_to_write.writelines(data)
    print(f'Write data to {write_file}')
