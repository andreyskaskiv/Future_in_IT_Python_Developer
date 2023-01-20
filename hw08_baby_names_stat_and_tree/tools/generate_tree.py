import os


def generate_tree(folder: str):
    """Generate the file names in a directory tree"""
    tree = []
    for address, dirs, files in os.walk(folder):
        path = address.split(os.sep)
        if '__pycache__' in address:
            continue
        row = f"{(len(path) - 1) * '|___'}{os.path.basename(address)}\n"
        tree.append(row)
        for file in files:
            row = f"{len(path) * '|___'}{file}\n"
            tree.append(row)

    return tree
