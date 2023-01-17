import os
import sys
from pathlib import Path

import hw10_race_report_framework

print('\n')

base_dir = Path(hw10_race_report_framework.__file__)
print(f'--> base_dir __init__=  {base_dir}')

base_dir_parent = Path(hw10_race_report_framework.__file__).parent
# path_to_config = os.path.join(base_dir, configfile)
print(f'--> base_dir_parent __init__=  {base_dir_parent}')
# print(f'--> path_to_config =  {path_to_config}')

base_dir_2_parent = Path(hw10_race_report_framework.__file__).parent.parent
print(f'--> base_dir_2_parent __init__=  {base_dir_2_parent}')

base_dir_3_parent = Path(hw10_race_report_framework.__file__).parent.parent.parent
print(f'--> base_dir_3_parent __init__=  {base_dir_3_parent}')

base_dir_sys = sys.path[0]
# path_to_config_sys = os.path.join(base_dir_sys, configfile)
print(f'--> base_dir_sys __init__ =  {base_dir_sys}')
# print(f'--> path_to_config_sys =  {path_to_config_sys}')

print('\n')

