import configparser
from hw8_baby_names_stat_and_tree.DTO.DTO import (Gender,
                                                  Identification)


class Config:
    def __init__(self):
        self.configfile = None

    def _get_config(self, configfile: str = 'config\config.ini'):
        self.configfile = configfile
        config = configparser.ConfigParser()
        config.read(configfile)
        return config

    def identification(self):
        username = self._get_config()['identification']['username']
        password = self._get_config()['identification']['password']
        token = self._get_config()['identification']['token']
        return Identification(username, password, token)

    def banned(self):
        list_of_banned_names = self._get_config()['ban-names']['names'].split(', ')
        return list_of_banned_names

    def get_gender(self):
        boys = self._get_config()['gender']['gender'].split(', ')[0]
        girls = self._get_config()['gender']['gender'].split(', ')[1]
        return Gender(boys, girls)

    def show_all_names(self):
        show_all_names = self._get_config()['ban-names-on_off']['show_all_names']
        return show_all_names

    def get_path_to_folder(self):
        path_to_folder = self._get_config()['path']['PATH_TO_FOLDER']
        return path_to_folder

    def get_quantity(self):
        quantity = self._get_config()['default-output']['quantity']
        return quantity

    def get_names_filter_file(self):
        baby_names_filter = self._get_config()['NAMES_FILTER_FILE']['BABY_NAMES_FILTER']
        return baby_names_filter
