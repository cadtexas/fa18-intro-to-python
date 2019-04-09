def parrot():
    """ Repeats whatever you say """
    message = input("*SQUAWK* Tell me something!")
    print("*SQUAWK* " + message + " *SQUAWK*")
    
def can_vote():
    age = input("How old are you? ")
    if age >= 18:
        return True

def even_odd():
  active = True
  user_in = ""
  while active:
    user_in = input("Enter a number and I will tell you if it is even or odd: ")
    if user_in != "quit":
      user_in = int(user_in)
      if (user_in % 2 == 0):
        print("Your number is even")
      else:
        print("Your number is odd")
    else:
      active = False

def parrot_while_var():
    """ Repeats whatever you say """
    message = ""
    while message != "quit":
        message = input("*SQUAWK* Tell me something! ")
        print("*SQUAWK* " + message + " *SQUAWK*")
    print("Goodbye!")

def parrot_while_flag():
    """ Repeats whatever you say """
    active = True
    message = ""
    while active:
        message = input("*SQUAWK* Tell me something! ")
        if message == 'quit':
            active = False
        else:
            print("*SQUAWK* " + message + " *SQUAWK*")
    print("Goodbye!")

def parrot_while_break():
    """ Repeats whatever you say """
    while True:
        message = input("*SQUAWK* Tell me something! ")
        if message == 'quit':
            break
        else:
            print("*SQUAWK* " + message + " *SQUAWK*")
    print("Goodbye!")
