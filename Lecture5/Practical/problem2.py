
def even (*argv):
    c=[x for x in argv if x%2==0]
    print(c)
    return(len(c))
print(even(2,3,4,5,6,7,8,12))
