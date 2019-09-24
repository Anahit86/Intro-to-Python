#####1#######
list2=[3,5,7,6,44,55,6,3,1]
print(list2)
S = len([n for n in list2 if n in range(5,10)])
print(S)

######2######
list4= [[10, 20, 40], [40, 50, 60],[70, 80, 90]]

list5=[ x[:-1] + [100] for x in list4 ]
print(list4)
print(list5)
