import argparse
#####N3########
list2= ["kk", 4, 2 , "yy",6, 4]
parser= argparse.ArgumentParser()
parser.add_argument("num", help ="insert some digit", type= int)
args= parser.parse_args()
count = list2.count(args.num)
print("list2:", list2)
print("number of %ds =" %(args.num), count)

######N4########
list4 = ["kk", 4, 2 , "yy",6, 4]
print("list4:", list4)
list4.remove(args.num)
print(args.num)
print("list4_after_remove:", list4)
