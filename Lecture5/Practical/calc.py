import pretty_print
def calculate_cube(x):
    y = x**3
    return(y)

def calculate_square(x):
    y= x**2
    return(y)

def main():
    #result=calculate_square(2)
    pretty_print.sample_print(calculate_square(2))
    #result1=calculate_square(4)
    pretty_print.pro_print(calculate_square(4))
if __name__=="__main__":
    main()
