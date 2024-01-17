#The user is asked to input their age to determine the person's stage of life.
age= int(input("Input your age:"))

#If age is lesser than or equal to 2 
if age<=2:
    print ("You are a baby")
#Prints the statement "You are a baby"

#If age is lesser than or equal to 4
elif age<=4:
    print ("You are a toddler")
#Prints the statement "You are a toddler"

#If age is lesser than or equal to 13
elif age<=13:
    print ("You are a kid")
#Prints the statement "You are a kid"

#If age is lesser than or equal to 20
elif age<=20:
    print ("You are a teenager")
#Prints the statement "You are a teenager"

#If age is lesser than or equal to 65
elif age<=65:
    print ("You are an adult")
#Prints the statement "You are an adult"

#If the age is 65 to above
else: 
    print("You are an elder")
#Prints the statement "You are an elder"