# List copying without slicing
my_schedule = ["Jazz", "Basket Weaving", "Japanese", "Intro to Python"]
my_schedule2 = my_schedule

my_schedule2.append("PE")
print("my_schedule:")
print(my_schedule)
print("my_schedule2:")
print(my_schedule2)

# Note that the change we applied to my_schedule2
# ended up affecting the original my_schedule!
# This is because my_schedule2 is not a copy of my_schedule,
# but is another variable that points to the original my_schedule
print()



# Copying using list slicing
schedule = ["Jazz", "Basket Weaving", "Japanese", "Intro to Python"]
schedule2 = schedule[:]

schedule2.append("PE")
print("schedule:")
print(schedule)
print("schedule2:")
print(schedule2)
# Now our output is as expected