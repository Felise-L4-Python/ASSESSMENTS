#Here's the code, items, and the price
a = {'Code': 'A30', 'Item': 'Lays', 'Price': 3} 
b = {'Code': 'B29', 'Item': 'Cheetos', 'Price': 3.5}
c = {'Code': 'C77', 'Item': 'Chupa Chups', 'Price': 2.5}
d = {'Code': 'E54', 'Item': 'Iced Coffee', 'Price': 4}
e = {'Code': 'F65', 'Item': 'Sprite', 'Price': 5}
f = {'Code': 'G10', 'Item': 'Egg Sandwich', 'Price': 7}
g = {'Code': 'H02', 'Item': 'Water', 'Price': 1}

#List of items
items = [a, b, c, d, e, f, g] 
money = 0

#A visual display
print("______________")
print("||   JCJ    ||")
print("|| ┌──────┐ ||")
print("|│ ![][][]! |│")
print("|| -------- ||")
print("|│ ![][][]! |│")
print("||  ┌────┐  ||")
print ("")
print("Greetings! Welcome to JCJ Vending Machine")

#The variables are the items and its assigning it to the prices.
Lays = 3 
Cheetos = 3.5
Chupa_Chups = 2.5
Iced_Coffee = 4
Sprite = 5
Egg_Sandwich = 7
Water = 1

#Defining prints out the 'items avaible' and the 'code' and 'price' once the code is activated
def show(items):
    print('\nItems available \n')
    print("======")
    for item in items:
        print(item.get('Code'), item.get('Item'), item.get('Price'))

print("")
money =float(input("Insert money: ")) #It lets the user to input the amount of money they want
buyagain = True #This makes it true so the code is on 

while buyagain == True: #This starts the loop for the user when buying from the vending machine
    show(items) #This prints the codes
    print("======")
    print("")
    choices = input("Input code: ") #This allows the user to input the code of the item they want to buy
    print("")

    if choices == 'A30': #If code A30 is selected, it will go through this path
        print("Item selected = Lays | Price = 3 ") #this code prints the item that has been selected and its price
        if money < Lays: #if the user's amount of money is less than the price of the product, the code will say "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= Lays: #if the user's amount of money is greater or equal to the price of the product, the code will continue
            money -= Lays #the vending machine will take the user's money and minus it from the price of the product
            print('Change returned: ' + str(money) + "\nYour Lays has been dispensed.") #the code will print the amount of money the user has left
        #the code will inform the user that the product has been dispensed

    elif choices == 'B29': #if item code 102 is selected, the user will go through this path
        print("Item selected = Cheetos | Price = 3.5 ") #this code prints the item that has been selected and its price
        if money < Cheetos: #if the user's amount of money is less than the price of the product, the code will say "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= Cheetos: #if the user's amount of money is greater or equal to the price of the product, the code will continue
            money -= Cheetos #the vending machine will take the user's money and minus it from the price of the product
            print('Change returned: ' + str(money) + "\nYour Cheetos has been dispensed.") #the code will print the amount of money the user has left
        #the code will inform the user that the product has been dispensed

    elif choices == 'C77': #if item code 103 is selected, the user will go through this path
        print("Item selected = Chupa Chups | Price = 2.5 ") #this code prints the item that has been selected and its price
        if money < Chupa_Chups: #if the user's amount of money is less than the price of the product, the code will say "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= Chupa_Chups: #if the user's amount of money is greater or equal to the price of the product, the code will continue
            money -= Chupa_Chups #the vending machine will take the user's money and minus it from the price of the product
            print('Change returned: ' + str(money) + "\nYour Chupa Chups has been dispensed.") #the code will print the amount of money the user has left
        #the code will inform the user that the product has been dispensed

    elif choices == 'E54': #if item code 104 is selected, the user will go through this path
        print("Item selected = Iced Coffee | Price = 4 ") #this code prints the item that has been selected and its price
        if money < Iced_Coffee: #if the user's amount of money is less than the price of the product, the code will say "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= Iced_Coffee: #if the user's amount of money is greater or equal to the price of the product, the code will continue
            money -= Iced_Coffee #the vending machine will take the user's money and minus it from the price of the product
            print('Change returned: ' + str(money) + "\nYour Iced Coffee has been dispensed.") #the code will print the amount of money the user has left
        #the code will inform the user that the product has been dispensed

    elif choices == 'F65': #if item code 105 is selected, the user will go through this path
        print("Item selected = Sprite | Price = 5 ") #this code prints the item that has been selected and its price
        if money < Sprite: #if the user's amount of money is less than the price of the product, the code will say "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= Sprite: #if the user's amount of money is greater or equal to the price of the product, the code will continue
            money -= Sprite #the vending machine will take the user's money and minus it from the price of the product
            print('Change returned: ' + str(money) + "\nYour Sprite has been dispensed.") #the code will print the amount of money the user has left
        #the code will inform the user that the product has been dispensed

    elif choices == 'G10': #if item code 106 is selected, the user will go through this path
        print("Item selected = Egg Sandwich | Price = 7 ") #this code prints the item that has been selected and its price
        if money < Egg_Sandwich: #if the user's amount of money is less than the price of the product, the code will say "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= Egg_Sandwich: #if the user's amount of money is greater or equal to the price of the product, the code will continue
            money -= Egg_Sandwich #the vending machine will take the user's money and minus it from the price of the product
            print('Change returned: ' + str(money) + "\nYour Egg Sandwich has been dispensed.") #the code will print the amount of money the user has left
        #the code will inform the user that the product has been dispensed

    elif choices == 'H02': #if item code 107 is selected, the user will go through this path
        print("Item selected = Water | Price = 1 ") #this code prints the item that has been selected and its price
        if money < Water: #if the user's amount of money is less than the price of the product, the code will say "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= Water: #if the user's amount of money is greater or equal to the price of the product, the code will continue
            money -= Water #the vending machine will take the user's money and minus it from the price of the product
            print('Change returned: ' + str(money) + "\nYour Water has been dispensed.") #the code will print the amount of money the user has left
        #the code will inform the user that the product has been dispensed

    else: #if the code that the user inputted is not one of the product's codes, it will print "Invalid code"
        print("Invalid code")

    choice = input('Do you want buy something else? (yes/no): ') #this code gives the user the choice of if they want to purchase another item or not
    if choice == 'no': #if the user inputs "n" it goes through this path
        PurchaseAgain = False #the loop stops

        if money != 0: #if money is not equal to 0, the code goes through this path
            print(str(money) + ' money left') #this prints the amount of money the user has left
            money = 0 #this makes the amount of money return to zero
            print('Thank you for buying, come again soon!\n')
            break
        else: #if money is equal to 0, the code just prints the final message
            print('Thank you for buying, come again soon!\n')
            break
    else: #if the user inputs "y" the code loops back to "PurchaseAgain"
        continue