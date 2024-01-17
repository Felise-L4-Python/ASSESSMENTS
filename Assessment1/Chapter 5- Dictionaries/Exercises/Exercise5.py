pets = [] #the variable "pets" is turned into a list

pet = {
    'Animal type': 'Dog',
    'Name': 'Chachim',
    'Owner': 'Grace',
} #the variable "pet" is turned into a dictionary
pets.append(pet) #adds the dictionary to the list

pet = {
    'Animal type': 'Cat',
    'Name': 'Theo',
    'Owner': 'Christine',
} #the variable "pet" is turned into a dictionary
pets.append(pet) #adds the dictionary to the list

pet = {
    'Animal type': 'Dog',
    'Name': 'Princess',
    'Owner': 'Mj',
} #the variable "pet" is turned into a dictionary
pets.append(pet) #adds the dictionary to the list

pet = {
    'Animal type': 'Cat',
    'Name': 'Yunie',
    'Owner': 'Jm',
} #the variable "pet" is turned into a dictionary
pets.append(pet) #adds the dictionary to the list

for pet in pets:
    print(f"\nHere's a little information about {pet['Name'].title()}:") #prints the statement in this line and the name of the pet in each dictionary
    for key, value in pet.items():
        print(f"\t{key}: {value}") #prints the age and animal type the pet is