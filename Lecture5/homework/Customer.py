import  Productcheck

def buy(product,num,price):
    if Productcheck.check(product,num):
        print("You bought" , product, "and spent", num*price)
    else:
        print("Sorry,we are out of this product")

def main():
    buy("candy", 5, 100)

if __name__=="__main__":
    main()
