guests = ['Cymon', 'Angel', 'Grace'] #variable "guests" becomes a list with 3 names

name = guests[0].title() #This assigns to the first name on the list
print(name + ", let's go out and have dinner together.") #prints the statement with the data stored in the variable "name"

name = guests[1].title() #This assigns to the second name on the list
print(name + ", let's go out and have dinner together.") #prints the statement with the data stored in the variable "name"

name = guests[2].title() #This assigns to the third name on the list
print(name + ", let's go out and have dinner together.") #prints the statement with the data stored in the variable "name"

name = guests[0].title() #This assigns to the first name on the list
print( "\nLooks like " + name + " can't come to dinner.") #prints the statement with the data stored in the variable "name"


del(guests[0]) #This deletes the first name on the list
guests.insert(0, 'Christine') #This inserts a new name and replaces the old name on the list

# Print the invitations again with the replaced name.
name = guests[0].title() #This assigns to the first name on the list
print("\n" + name + ", let's go out and have dinner together.") #prints the statement with the data stored in the variable "name"

name = guests[1].title() #This assigns to the second name on the list
print(name + ", let's go out and have dinner together.") #prints the statement with the data stored in the variable "name"

name = guests[2].title() #This assigns to the third name on the list
print(name + ", let's go out and have dinner together.") #prints the statement with the data stored in the variable "name"