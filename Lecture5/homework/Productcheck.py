products = {"candy":10, "juice": 5, "pen":50}
def check(product,num):
    if product in products.keys():
        if num <= products[product]:
            return True
        else:
            return False

check("candy", 7)
