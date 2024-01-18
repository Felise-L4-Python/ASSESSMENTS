sandwich_orders = ['Pastrami', 'BLT', 'Egg', 'Pastrami', 'Bacon', 'Pastrami', 'Grilled Chicken'] #The variable turns into a list that has 4 different orders.
finished_sandwiches = [] #variable "finished_sandwiches" turns into an empty list

print("It looks like we have run out of Pastrami today, my apologies") #This prints the statement.
while 'Pastrami' in sandwich_orders: 
    sandwich_orders.remove('Pastrami') #This removes 'pastrami' from the list "sandwich_orders"

print ('\n')
while sandwich_orders: #while "sandwich_orders" is true
    current_sandwich = sandwich_orders.pop() #The variable "current_sandwich" is assigned the retrieved data from "sandwich_orders"
    print(f"Your {current_sandwich} sandwich is being made.") #Here prints the statement and the data in "current_sandwich"
    finished_sandwiches.append(current_sandwich) #Here adds the data stored in "current_sandwich" to the list "finished_sandwiches"

print ('\n')
for sandwich in finished_sandwiches:
    print(f"Here's your {sandwich} sandwich.") #This prints the statement and in the list "finished_sandwiches"

