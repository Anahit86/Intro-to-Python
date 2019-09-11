a = [1,4,5,7,8,-2,0,-1]
print(a[3], a[5])
a_sorted = sorted(a, reverse=True)
print(a_sorted)
print(a_sorted[1:4] ,"\n", a_sorted[2:7])
a_sorted.pop(3)
a_sorted.pop(2)
print(a_sorted)
b= ["grapes","patatoes","tomatoes","orange","lemon","brocoli","carrot","sausages"]
b_sorted=sorted(b)
print(b_sorted)
c = a[1:4] + b[4:7]
print(c)
