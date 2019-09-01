import argparse

set3= {1,2,3,4,5,6,77,44}
parser= argparse.ArgumentParser()
parser.add_argument("num", help = "insert some digit", type= int)
args = parser.parse_args()
print(args.num in range(min(set3),max(set3)))
