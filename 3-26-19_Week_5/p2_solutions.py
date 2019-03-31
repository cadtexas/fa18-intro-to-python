'''
Week 5: Programming Assignment 1 SOLUTIONS:
https://codingbat.com/prob/p137202

The comments try to explain the code in words. 
The explanations in parentheses are IMPLIED but not explicitly coded.

EXTRA: We don't need 'else' in the second return (line 20) for function round10(num). Instead, we put it outside of any condition. Why?
ANS: Since returning exits the function immediately, we don't need to worry about the program executing the code after the return statement. If the code doesn't go through the if statement, the condition must have evaluated to False, which means we need to execute the second return statement. Since that is the only other case, and it won't execute if the condition is True, we can put it on the outside.
'''

def round_sum(a, b, c):
	return round10(a) + round10(b) + round10(c)
 
def round10(num):
	# if the last digit is greater than or equal to 5, round the value up
	if num % 10 >= 5:
		return num + 10 - (num % 10)
	# otherwise, round the value down
	return num - (num % 10)  