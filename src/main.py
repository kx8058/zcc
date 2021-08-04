import json
import requests
# import ../config/data.py   # line below might be a better candidate 
from data import *

# if the user were to enter 'menu'
def picked_menu():
	menu_choice = input("You have picked 'menu'. Here are the next options:")
	print("* Enter '1' to view all of the tickets.")
	print("* Enter '2' to view a ticket.")
	print("* Enter 'quit' to exit.")

	if menu_choice != '1' and menu_choice != '2' and menu_choice != 'quit':  # if the user entered neither of the 3 given choices
		print("Sorry, I don't think you entered one of the given choices. Please try again.")
	elif menu_choice == '1':   # if user wanted to see all of the tickets, in this case it is just the name of each group
		name_each_group()
	elif menu_choice == '2':   # if user wanted to see a ticket
		first_group()
	else:  # if user entered 'quit'
		print("You have picked 'quit'. Thank you for using the viewer. Goodbye!")

def main():
	print("Hello, welcome to the ticket viewer!")
	opening_choice = input("What would you like to do? To view the options, enter 'menu'. To exit, enter 'quit'.")
	
	if opening_choice != "menu" and opening_choice != "quit":   # if the user entered neither of the 2 given choices
		print("Sorry, I don't think you entered one of the given choices. Please try again.")
	elif opening_choice == "menu":
		picked_menu()
	else:	# if user entered 'quit'
		print("You have picked 'quit'. Thank you for using the viewer. Goodbye!")

main()

