'''
Week 5: Programming Assignment 1 SOLUTIONS:
https://codingbat.com/prob/p137202

The comments try to explain the if statements' contents in words. 
The explanations in parentheses are IMPLIED but not explicitly coded.

EXTRA: We don't need 'elif' here instead of 'if'. Can you think of why?
ANS: Since returning exits the function immediately, we don't need to worry about the program executing the code of multiple if statements. Once the function returns, the program will never execute the remaining code under the return statement.
'''

def caught_speeding(speed, is_birthday):
    # if speed is between 65 and 85 and it's your birthday
    if speed > 65 and speed <= 85 and is_birthday:
        return 1

    # otherwise, if your speed is above 85 and it's your birthday
    if speed >= 86 and is_birthday:
        return 2

    # otherwise, if your speed is below 65 and it's your birthday
    if speed <= 65 and is_birthday:
        return 0

    # otherwise, if your speed is between 60 and 80 (but it's not your birthday)
    if speed > 60 and speed <= 80:
        return 1

    # otherwise, if your speed is above 80 (but it's not your birthday)
    if speed >= 81:
        return 2

    # otherwise (if it's not your birthday and your speed is below 60)
    else: 
        return 0