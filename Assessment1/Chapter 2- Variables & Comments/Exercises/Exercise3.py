#The variable is assigned to the string.
name= "\tAyukei\n"

#This code prints the name
print ("Unmodified")
print (name)

#This code prints the name while removing the leading whitespace characters.
print("\nUsing lstrip():")
print(name.lstrip())

#This code prints the name while removing the trailing whitespace characters.
print("\nUsing rstrip():")
print (name.rstrip())

#This code prints the name while removing both the leading and the trailing whitespace characters.
print("\nUsing strip():")
print (name.strip())