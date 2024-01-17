#The variables is given the statements for this prompt, += will make both variables show in the terminal
prompt = "\n What topping would you like on your pizza?"
prompt += "\n Enter 'quit' when you're done:"

#The while loop becomes true
while True:
    topping = input(prompt)
    #This prints the variable and the user has to input their toppings
    if topping != 'quit':
        #If the user inputs their answer that is not 'quit'
        print (f"The {topping} are now added on your pizza")
#This prints the string and the topping of the user's choice
    else:
        break
    #This ends the code when the user input 'quit'