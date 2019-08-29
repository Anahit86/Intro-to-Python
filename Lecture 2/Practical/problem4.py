import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--age", help = "insert the number" , type=int)
args = parser.parse_args()

if args.age:
    print ("happy birthday, you are already" ,  args.age,  "years old")
