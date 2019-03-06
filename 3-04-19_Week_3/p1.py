import grader

'''
Week 3: Programming Assignment 1
You have a list of strings that hold the names of the classes that we're in. This program will have three steps:
1. You want to add two classes to your schedule named "Organic Chemistry" and "Modern Physics". You want to add "Organic Chemistry" as your first class of the day and "Modern Physics" as your last class of the day. 
2. You decide that taking "Organic Chemistry" at 8 in the morning is too much. You want to remove it from your schedule.
3. Store your second class of the day in the variable named period_2.
'''

schedule = ["Discrete Math", "Data Structures", "Computer Architecture"]

# Step 1: Add "Organic Chemistry" to the front of the list and "Modern Physics" to the end of the list. Write your code under this line! This can be done in two lines of code.



grader.grade11(schedule) # You can ignore this line! This is just for testing your code. :)
#-----------------------------------------------------------------------------------------------------#

# Step 2: Remove "Organic Chemistry" from this list. This can be done in two ways, either is fine for this problem. This can be done in just one line of code.



grader.grade12(schedule) # You can ignore this line! This is just for testing your code. :)
#-----------------------------------------------------------------------------------------------------#

# Step 3: Store the second element of the list in the variable below! We do not want that element removed, however.

period_2 = "" # Modify this line of code using the 'schedule' list


grader.grade13(period_2, schedule) # You can ignore this line! This is just for testing your code. :)