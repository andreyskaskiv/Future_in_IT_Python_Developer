import os


def check_folder_exist(folder: str):
    """Check folder exist"""
    if not os.path.exists(folder):
        raise FileExistsError(f'Folder {folder} not exist')

    if not os.path.isdir(folder):
        raise TypeError(f'{folder} is not a folder')


def check_file_exist(filename: str):
    """Check if file exist"""
    if not os.path.exists(filename):
        raise FileExistsError(f'File {filename} not exist')

    if not os.path.isfile(filename):
        raise TypeError(f'{filename} is not a file')


def check_file_type(filename: str):
    """Check if txt file format"""
    try:
        open(filename).read()
    except UnicodeDecodeError:
        return False
    return True
