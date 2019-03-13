# Solution 1
rain = False 
test = False 
schedule = ["Wake up", "Go to class", "Sleep"]

if rain == True and test == True:
	schedule.insert(1, "Bring your umbrella!")
	schedule.insert(3, "Study for test!")
elif rain == True:
	schedule.insert(1, "Bring your umbrella!")
elif test == True:
	schedule.insert(-1, "Study for test!")
else:
    pass

print(schedule)

# Solution 2
schedule = ["Wake up", "Go to class", "Sleep"]
if not rain and not test:
    print(schedule)
if rain:
