filler = "-------------------------------"

def grade11(schedule):
	print(filler)
	correct = len(schedule) == 5 and ("Organic Chemistry" == schedule[0]) and ("Discrete Math" == schedule[1]) and ("Data Structures" == schedule[2]) and ("Computer Architecture" == schedule[3]) and ("Modern Physics" == schedule[4])
	if correct:
		print("Your code for Step 1 is correct!")
	else:
		print("Your code for Step 1 is incorrect. The list should be:")
		print('["Organic Chemistry", "Discrete Math", "Data Structures", "Computer Architecture", "Modern Physics"]')
		print("Your 'schedule' list was actually:")
		print(schedule)
	print(filler)

def grade12(schedule):
	correct = len(schedule) == 4 and ("Discrete Math" == schedule[0]) and ("Data Structures" == schedule[1]) and ("Computer Architecture" == schedule[2]) and ("Modern Physics" == schedule[3])
	if correct:
		print("Your code for Step 2 is correct!")
	else:
		print("Your code for Step 2 is incorrect. The list should be:")
		print('["Discrete Math", "Data Structures", "Computer Architecture", "Modern Physics"]')
		print("Your 'schedule' list was actually:")
		print(schedule)
	print(filler)

def grade13(per2, schedule):
	per2Correct = per2 == "Data Structures" 
	listCorrect = len(schedule) == 4 and ("Discrete Math" == schedule[0]) and ("Data Structures" == schedule[1]) and ("Computer Architecture" == schedule[2]) and ("Modern Physics" == schedule[3])
	correct = per2Correct and listCorrect
	if correct:
		print("Your code for Step 3 is correct!")
	if not per2Correct:
		print("Your variable doesn't store the second item of the list! The variable should hold 'Data Structures'")
		print("Your variable holds " + "'" + per2 + "'")
	if not listCorrect:
		print("Your list is incorrect. This list should be: ")
		print('["Discrete Math", "Data Structures", "Computer Architecture", "Modern Physics"]')
		print("Your 'schedule' list was actually:")
		print(schedule)
	print(filler)

def grade21():
	print(filler)
	print("Step 1 Answer:")
	print("This program should print 'Sean is an adult.' It should only contain one line of code.")
	print(filler)

def grade22():
	print(filler)
	print("Step 2 Answer:")
	print("The program should only be printing one line at at a time. In other words, the only output that should be printed is 'Sean can buy alcohol legally but not run for president.'")
	print(filler)

def hint22():
	print("HINT: Instead of having 'if', try changing them to 'elif' (like the problem above!) Can you see why the multiple if statements will print multiple things while the elif will only print 1?")