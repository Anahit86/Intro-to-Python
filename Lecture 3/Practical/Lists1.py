import sys
list1= ["hello", 1, True]
print(list1)
if len(sys.argv)>2:
    list1.extend(sys.argv[1:])
    print ("new_list1:", list1)
    print(sys.argv[1:])
