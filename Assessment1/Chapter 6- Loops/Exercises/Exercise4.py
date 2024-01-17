sandwich_orders = ['BLT', 'Egg', 'Bacon', 'Grilled Chicken'] #variable "sandwich_orders" turns into a list that has 4 different orders.
finished_sandwiches = [] #variable "finished_sandwiches" turns into an empty list

while sandwich_orders: #while "sandwich_orders" is true
    current_sandwich = sandwich_orders.pop() #The variable "current_sandwich" is assigned the retrieved data from "sandwich_orders"
    print(f"Your {current_sandwich} sandwich is being made.") #Here prints the statement in this line and the data in "current_sandwich"
    finished_sandwiches.append(current_sandwich) #Here adds the data stored in "current_sandwich" to the list "finished_sandwiches"

print("\n")
for sandwich in finished_sandwiches:
    print(f"Here's your {sandwich} sandwich.") #This prints the statement in this line and in the list "finished_sandwiches"