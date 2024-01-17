#variable "guests" becomes a list with 5 names.
guests = ['Cymon', 'Angel', 'Grace', 'Enrico', "Clark"]

name = guests[0].title()
print(name + ", let's go out and have dinner together.")

name = guests[1].title()
print(name + ", let's go out and have dinner together.")

name = guests[2].title()
print(name + ", let's go out and have dinner together.")

name = guests[0].title()
print("\nSorry, " + name + " can't make it to dinner.")

#This deletes the first name on the list and replaces a new name on the list.
del(guests[0])
guests.insert(0, 'Christine') #This inserts a new name and replaces the old name on the list.

#Then print the invitations again.
name = guests[0].title()
print("\n" + name + ", let's go out and have dinner together.")

name = guests[1].title()
print(name + ", let's go out and have dinner together.")

name = guests[2].title()
print(name + ", let's go out and have dinner together.")

#The table won't arrive on time, this prints the statement.
print("\nI'm sorry, I can only invite two people to dinner.")

# This removes the guests from the list until there's only two remaining names on the list.
name = guests.pop() 
print("Sorry, " + name.title() + " there's no room at the table.")

name = guests.pop()
print("Sorry, " + name.title() + " there's no room at the table.")

name = guests.pop()
print("Sorry, " + name.title() + " there's no room at the table.")


name = guests[0].title() #variable "name" is assigned the first name from the list.
print("Hello " + name + " Would you still like to go out for dinner?") #prints the statement

name = guests[1].title() #variable "name" is assigned the second name from the list.
print("Hello " + name + " Would you still like to go out for dinner?")

#This deletes the names on the list
del(guests[0])
del(guests[0])

#This is the proof that the list is empty.
print(guests)