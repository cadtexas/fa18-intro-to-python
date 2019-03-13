# Solution 1: Starting with an empty list
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

# Solution 2: Starting with a list containing the range 1-10.
squares2 = list(range(1,11))
for x in range(len(squares2)):
    squares2[x] = squares2[x] ** 2
print(squares2)


# Solution 3: Starting with a list containing the range 1-10
# Iterating without a range() object
# Note that this solution does not work
squares3 = list(range(1,11))
for square in squares3:
    square = square ** 2
# Note that the output is wrong and it never changes! This is because in Python, ints are 
# immutable. We will touch on this topic in week 5, after the break.
print(squares3)
