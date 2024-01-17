def make_shirt(size='large', message='I love Python'): #This defines the variable
    print(f"\nI'm going to make a {size} t-shirt.") #This prints the statement and the variable "size"
    print(f'In the shirt it will say "{message}".') #prints the statement and the variable "message"

make_shirt() 
make_shirt(size='medium') #stores the size to the variable "make_shirt"
make_shirt('Extra large', 'All too well') #stores the data to the variable "make_shirt"