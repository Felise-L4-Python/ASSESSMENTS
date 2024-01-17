country = ['Korea', 'Japan', 'Switzerland', 'Spain', 'Iceland'] #The variable 'country' becomes a list

print("Original order:")
print(country) #This prints the list in its original order

print("\nAlphabetical:")
print(sorted(country)) #This prints the list in alphabetical order

print("\nOriginal order:")
print(country) #This prints the list in its original order

print("\nReverse alphabetical:")
print(sorted(country, reverse=True)) #This prints the list in alphabetical order but in reverse

print("\nOriginal order:")
print(country) #This prints the list in its original order

print("\nReversed:")
country.reverse() #This reverse the order of the list
print(country) #This prints the list in its original order but in reverse

print("\nOriginal order:")
country.reverse() #This reverse the order of the list
print(country) #This prints the list in its original order

print("\nAlphabetical")
country.sort() #This sort the list order alphabetically
print(country) #This prints the list in alphabetical order

print("\nReverse Alphabetical")
country.sort(reverse=True) #It reverses the list order
print(country) #prints the list in its original order but in reverse