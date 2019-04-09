'''
Week 7: Programming Assignment 1 SOLUTIONS:
'''

# main method
def organize_birthday():
	name = input("What is your name? ")
	age = int(input("How old are you? "))
	guest_list = []
	guest = ""
	while True:
		guest = input("Who would you like to invite? Type 'done' when you are done. " )
		if guest == "done":
			break
		guest_list.append(guest)

	print_birthday(name, age)
	print_guests(guest_list)

# Prints the "Happy Xth Birthday, User!" message
def print_birthday(name, age):
	suffix = "th"
	if age % 10 == 1 and age != 11:
		suffix = "st"
	elif age % 10 == 2 and age != 12:
		suffix = "nd"
	elif age % 10 == 3 and age != 13:
		suffix = "rd"

	age_suffix = str(age) + suffix
	print("Happy " + age_suffix + " Birthday, " + name + "!")

# Prints the guest list in alphabetical order
def print_guests(guest_list):
	guest_list.sort()
	print("Guests to be Invited: ")
	for guest in guest_list:
		print(guest)

organize_birthday()