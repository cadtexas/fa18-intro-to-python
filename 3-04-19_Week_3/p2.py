import grader

'''
Week 3: Programming Assignment 2
Sean has an ID that contains his name and age. He wants to check his ID to see what actions he's allowed to do as a US citizen. This program will have 2 parts.
1. Before running the program, try to predict what our program will print.
2. Sean wants to fake his age to try to buy some alcohol. (CAD does not endorse underage drinking!) However, the ID checker at the store is broken and prints too many things! Can you figure out why?
You can also experiment around with different ages. Try changing citizen_age and citizen_fake_age to see what results gets produced!
'''

citizen_name = "Sean"
citizen_age = 19

# Step 1: What will this code output? How many lines will it print? Once you've answered that, run the program to check your answer.
print("Step 1 Output:")

if citizen_age > 65:
	print(citizen_name + " is a senior citizen.")
elif citizen_age > 18:
	print(citizen_name + " is an adult.")
elif citizen_age > 12:
	print(citizen_name + " is a teenager.")
else:
	print(citizen_name + " is a child.")


grader.grade21()
#-----------------------------------------------------------------------------------------------------#

# Step 2: Run the code below. It seems to be printing too many things! Fix the code below to output the right thing!
# HINT: The output should only be printing one line! Does it look like code you might have seen in the problem above?
print("Step 2 Output:")

citizen_fake_age = 22

if citizen_fake_age > 35:
	print(citizen_name + " can run for president.")
if citizen_fake_age > 21: # Fix this line!
	print(citizen_name + " can buy alcohol legally but not run for president.")
if citizen_fake_age > 18: # Fix this line!
	print(citizen_name + " can vote in elections but not buy alcohol legally or run for president.")
else:
	print(citizen_name + " is still a child and cannot do anything.")


# grader.hint22() # If you need a hint, uncomment (remove the first # sign from the front) the line below!
grader.grade22()