import configparser
import os
from pathlib import Path
import hw10_race_report_framework


def get_config(configfile: str):
    base_dir = Path(hw10_race_report_framework.__file__).parent
    path_to_config = os.path.join(base_dir, configfile)

    config = configparser.ConfigParser()
    config.read(path_to_config)
    return config, base_dir


def get_config_settings(config, base_dir):
    """Read in `defaults.cfg` to obtain default configuration values."""
    directory_int = config["SETTINGS"]["INPUT_DIRECTORY"]
    directory_out = config["SETTINGS"]["OUTPUT_DIRECTORY"]
    output_filename = config["SETTINGS"]["OUTPUT_FILENAME"]

    input_directory = os.path.join(base_dir, directory_int)
    output_directory = os.path.join(base_dir, directory_out)

    return input_directory, output_directory, output_filename


def get_config_parameters(config):
    """Read in `defaults.cfg` to obtain default configuration values."""
    save = config["PARAMETERS"]["SAVE"]
    private = config["PARAMETERS"]["PRIVATE"]
    return save, private