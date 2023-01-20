import os


def show_generate_tree(folder: str):
    """Generate the file names in a directory tree"""
    for address, dirs, files in os.walk(folder):
        path = address.split(os.sep)
        if '__pycache__' in address:
            continue
        print((len(path) - 1) * '|___', os.path.basename(address))
        for file in files:
            print(len(path) * '|___', file)

    return folder

