import argparse

parser = argparse.ArgumentParser()
parser.add_argument("ky", help="insert key value", type=str)
parser.add_argument("val", help="insert value for key", type=str)
args = parser.parse_args()
dict1 = {'key1': "anahit", 'key2': "kkk", 'nom': "ll"}
print (dict1)
dict1[args.ky] = args.val
print(dict1)
