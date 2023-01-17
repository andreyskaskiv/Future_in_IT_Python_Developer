from distutils.util import strtobool


def check_type(private):
    if isinstance(private, bool):
        private_check = private
    elif private in 'YN':
        private_check = strtobool(private)
    else:
        private_check = True
    return private_check