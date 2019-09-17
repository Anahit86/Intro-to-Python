def pswd (password):

    if len(password) >=10 and len([x for x in password if x.isdigit()]) >=2:
        print(True)
    else:
        print(False)
pswd("afasj7dkhsf6kjhffad")
