medical = input("do you have a medical reason? (y/n):")
if medical == "y":
    print("you are allowed")
else:
    attendance=int (input("enter attendance percentage"))

    if attendance >= 85:
        print ("you are allowed")
    else:
        print("you are not allowed")


