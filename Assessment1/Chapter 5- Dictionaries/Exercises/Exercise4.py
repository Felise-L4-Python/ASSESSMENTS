rivers = {
    'Yangtze' : 'China',
    'Mississippi' : 'United States',
    'Missouri' : 'United States'
} #The variable 'rivers' is stored data including the names of the rivers and where it runs through.

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.") #This prints the river names and the country it is located to.

print("\nThis dictionary includes the following rivers:") #This prints the statement in this line
for river in rivers.keys():
    print(f"- {river.title()}")  #This prints the river names

print("\nThis dictionary includes the following countries:") #This prints the statement in this line
for country in rivers.values():
    print(f"- {country.title()}") #This prints the country names