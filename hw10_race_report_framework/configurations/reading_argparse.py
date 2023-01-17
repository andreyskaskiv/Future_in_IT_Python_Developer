import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        prog='CLI Interface to hw10_race_report_framework',
        usage='%(prog)s cli_report.py '
              '[--files "<path to folder>"] '
              '[--asc | --desc] '
              '[--driver] '
              '[--save default "Y"] '
              '[--private default "Y"]',
        description='Show report about racing logs')
    parser.add_argument(
        '-f',
        '--files',
        type=str,
        help='path to folder with txt files',
        required=False)
    parser.add_argument(
        '--asc',
        action='store_true',
        help='ordering by ascending',
        default=False,
        required=False)
    parser.add_argument(
        '--desc',
        action='store_true',
        help='ordering by ascending',
        default=False,
        required=False)
    parser.add_argument(
        '-d',
        '--driver',
        type=str,
        help='show information about driver',
        default='',
        required=False)
    parser.add_argument(
        "--save",
        help="Save file? default 'Y'",
        default=None,
        required=False)
    parser.add_argument(
        '-p',
        "--private",
        help="Hide the first three places? default 'Y'",
        default=None,
        required=False)
    args = parser.parse_args()
    return args


def get_argparse():
    args = parse_args()
    argvs_input_directory = args.files
    argvs_save = args.save
    argvs_private = args.private
    order_asc = args.asc
    order_desc = args.desc
    driver = args.driver
    return argvs_input_directory, argvs_save, argvs_private, order_asc, order_desc, driver
