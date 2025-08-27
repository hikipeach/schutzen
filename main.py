import argparse

parser = argparse.ArgumentParser(prog='schutzen')
subparsers = parser.add_subparsers()

#init command
parser_init = subparsers.add_parser('i', 'init', help='init help')

args = parser.parse_args()
