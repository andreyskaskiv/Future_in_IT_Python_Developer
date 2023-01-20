"""Handle file errors"""


def check_file(filename: str):
    """Check exist file and txt format"""
    try:
        with open(filename, mode='rt') as file:
            file.read()
    except FileNotFoundError as error:
        return error
    except UnicodeDecodeError:
        return 'Application works only with txt files.'
