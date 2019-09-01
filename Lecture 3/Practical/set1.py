import argparse

set1= {1, 7, "Anahit"}
print("before_change:",set1)
parser= argparse.ArgumentParser()
parser.add_argument("value", help="insert some value", type=int)
args=parser.parse_args()
set1.add(args.value)
print("after_change:", set1)
