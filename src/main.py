import json
import requests

def main():
	print("Hello, welcome to the ticket viewer!")
	opening_choice = input("What would you like to do? To view the options, type 'menu'. To exit, type 'quit'.")
	if opening_choice != "menu" and opening_choice != "quit":
		print("Sorry, I don't think you entered one of the given choices. Please try again.")
	elif opening_choice == "menu":
		picked_menu()
	else:
		print("You have picked 'quit'. Thank you for using the viewer. Goodbye!")

main()

