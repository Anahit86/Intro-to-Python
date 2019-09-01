import argparse

set2= {"Anahit", 4, 5, 7,"ll"}

parser = argparse.ArgumentParser()
parser.add_argument("val", help ="insert some value", type=int)
args= parser.parse_args()

set2.remove(args.val)
print(set2)
