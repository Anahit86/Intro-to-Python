import argparse

parser = argparse.ArgumentParser()
parser.add_argument("str", help="insert 7 and more length string", type=str)
args= parser.parse_args()
print("the old string:", args.str)
l = len(args.str)//2
print("middle 3 charecters:", args.str[l-1:l+2])
print("the new string:", args.str[0:l-1]+args.str[l-1:l+2].upper() + args.str[l+2:])
