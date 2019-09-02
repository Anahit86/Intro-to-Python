import argparse

parser = argparse.ArgumentParser()
parser.add_argument("text", help = "insert some text", type = str)
args= parser.parse_args()
print("the given string is:", args.text)
print("The USA count is:", args.text.lower().count("usa"))
print("the new string is:", args.text.replace("USA", "Armenia"))
