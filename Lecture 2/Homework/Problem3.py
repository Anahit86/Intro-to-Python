import argparse

parser = argparse.ArgumentParser()
parser.add_argument("text", help="insert some text", type= str)
parser.add_argument("str1", help= "insert string", type= str)
parser.add_argument("str2", help= "insert some string", type = str)
args= parser.parse_args()
print("the given text is:" ,args.text)
print("the first word is:" ,args.str1)
print("the second word is:", args.str2)
print("output is:", args.text.replace(args.str1,args.str2))
