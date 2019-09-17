##########problem1###########
for x in range(11):
    if x%2==0:
        continue
    print(x)

###########problem2#############
list1= [1,3,5,7,9,11,13,15]
list2=[4,6,14,11,8,16]
for l1 in list1:
    for l2 in list2:
        if l1==l2:
            break
            print(l1)

#########problem3#########
menu= ['ice_cream', 'chocolate','apple crips','cookies']
desert = input()
while desert not in menu:
    print("please chosse another deser")
    desert= input("enter another desert")
    if desert in menu:
        print("Your dessert will arive in 10minutes")
