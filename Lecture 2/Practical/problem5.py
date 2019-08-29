import argparse

parser= argparse.ArgumentParser()
parser.add_argument("str", help ="insert some string", type = str)
args = parser.parse_args()
print(args.str.upper())
print(args.str.lower())
