import sys
list1= ["hello", 1, True]
new_list = list1.copy()
print(list2)
print(list1)
if len(sys.argv)>2:
    new_list.extend(sys.argv[1:])
    print ("new_list2:", new_list)
    print ("list1:", list1)
