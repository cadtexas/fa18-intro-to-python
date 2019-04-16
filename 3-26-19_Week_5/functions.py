people = ["Claire", "Hannah", "Sean"]
programming_languages = ["Python", "Java"]
def length(some_list):
    length = 0
    for element in some_list:
        length += 1
    print(length)

length(people)
length(programming_languages)