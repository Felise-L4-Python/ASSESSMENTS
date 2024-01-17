#Write a program that calculates how many USB sticks a girl can buy and how many pounds she will have left.

#The variable which has the value of the girl's budget.
budget= 50

#Calculate how many USB sticks can be bought.
USB_Sticks= budget // 6

#Calculate how many pounds are left after buying the USB sticks
remaining_budget= budget % 6

#Print the number of USB sticks the girl can buy and how many pounds she will have left.
print ("The girl can buy", USB_Sticks, "USB sticks and will have", remaining_budget, "pounds left.")
