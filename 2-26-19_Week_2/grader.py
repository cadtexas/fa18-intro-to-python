filler = "------------------------------------------"

def grade1(answer):
	solution = "Sean is an instructor of Intro to Python!"
	if answer == solution:
		print("Programming Assignment 1 --- PASS!")
	else:
		print("Programming Assignment 1 --- INCORRECT")
		print(filler)
		print("What combined_message should store: ")
		print("Sean is an instructor of Intro to Python!")
		print(filler)
		print("What your code's combined_message stored: ")
		print(answer)

def grade2(p1, p2):
	p1_ans = False
	p2_ans = False
	if p1 == "Sean scored 4th place at the coding competition!":
		p1_ans = True
	if p2 == "Claire scored 5th place at the coding competition!":
		p2_ans = True

	if p1_ans and p2_ans:
		print("Programming Assignment 2 --- PASS!")
	else:
		print("Programming Assignment 2 --- INCORRECT")
		if not p1_ans and not p2_ans:
			print("Both sentences were incorrect.")
		elif not p1_ans:
			print("Sentence 1 was incorrect.")
		else:
			print("Sentence 2 was incorrect.")
		print(filler)
		print("What your sentence_1 and sentence_2 stored:")
		print("sentence_1: " + p1)
		print("sentence_2: " + p2)