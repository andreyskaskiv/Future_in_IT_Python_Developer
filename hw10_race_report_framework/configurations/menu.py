from distutils.util import strtobool

from hw10_race_report_framework.configurations.reading_argparse import get_argparse
from hw10_race_report_framework.configurations.reading_config import (get_config,
                                                                      get_config_settings,
                                                                      get_config_parameters)

DEFAULTS = "defaults.cfg"


def menu():
    config, base_dir = get_config(DEFAULTS)
    def_input_directory, def_output_directory, def_output_filename = get_config_settings(config, base_dir)
    def_save, def_private = get_config_parameters(config)

    argvs_input_directory, argvs_save, argvs_private, order_asc, order_desc, driver = get_argparse()

    directory_input = argvs_input_directory if argvs_input_directory else def_input_directory

    def_save_ind = True if def_save.upper() == "Y" else False
    final_save = argvs_save if argvs_save is not None and strtobool(argvs_private) else def_save_ind
    def_private_ind = True if def_private.upper() == "Y" else False
    final_private = argvs_private if argvs_private is not None else def_private_ind

    return (directory_input, final_save, final_private, def_output_directory, def_output_filename,
            order_asc, order_desc, driver)