import grader

'''
Week 2: Programming Assignment 2

The program currently returns an error! Please fix it so that it will return the right thing. You can 
solve this in two ways. Try both!
1. Change lines 22 and 23
2. Change line 25 and 26

sentence_1 should store "Sean scored 4th place at the coding competition!"
sentence_2 should store "Claire scored 5th place at the coding competition!"
'''

person_1 = "Sean"
person_2 = "Claire"

message = " place at the coding competition!"
fourth = 4   # Modify this line for solution 1
fifth = 5    # Modify this line for solution 1

sentence_1 = person_1 + " scored " + fourth + "th" + message   # Modify this line for solution 2
sentence_2 = person_2 + " scored " + fifth + "th" + message    # Modify this line for solution 2

# You can ignore this line! This is just for testing your code. :)
grader.grade2(sentence_1, sentence_2)