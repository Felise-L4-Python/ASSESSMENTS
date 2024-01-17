#This variable asks the user how old are they.
lines = "How old are you?:"

#The while loop will become true
while True:
    age= input(lines)    
    #This will make the user give their given age 
    age = int(age)

    if age <3:
        print ("The ticket is free!")
        #If the user's age is below 3, it will print the ticket is free

    elif age <= 12:
        print ("The ticket is $10")
        #If the user's age is lesser than or equal to 12, it will print the price of the ticket

    else:
        print ("The ticket is $15")
        #If the user's age is over the age of 12, this will print the price of the ticket. 