import os
import argparse


DEFAULT_DIR = os.getcwd()


def parse_args():
    parser = argparse.ArgumentParser(description='Download page')
    parser.add_argument('url')
    parser.add_argument('-o', '--output',
                        default=DEFAULT_DIR,
                        help='directory of output')
    return parser.parse_args()
