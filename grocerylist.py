print("welcome to your grocery list")

userInp = 0
grocerylist = []

def printInstructions():
    print("What would you like to do? \n1. add item to list \n2. remove item from list \n3. read list \n4. exit")
    global userInp
    userInp = int(input(">> "))
    print("\n")

    if userInp < 1 or userInp > 4 :
        print("that's an invalid entry")
        printInstructions()



printInstructions()

while userInp != 4:
    if userInp == 1:    
        print("What do you want to add to the list? ")
        groceryitem = input(">> ")
        grocerylist.append(groceryitem)
        print("{} added to your list \n".format(groceryitem))

    if userInp == 2:
        print("What do you want to remove from the list? ")
        groceryitem = input(">> ")
        for item in grocerylist:
            if item == groceryitem:
                grocerylist.remove(groceryitem)
                print("{} has been removed from your list \n".format(groceryitem))
                break
            print("{} is not in your list \n".format(groceryitem))

    if userInp == 3:
        if grocerylist:
            print("Your list:")
            print("---------------------")
            for item in grocerylist:
                print("{}".format(item))
            print("---------------------\n")
        else:
            print("Your list is empty\n")
    printInstructions()


