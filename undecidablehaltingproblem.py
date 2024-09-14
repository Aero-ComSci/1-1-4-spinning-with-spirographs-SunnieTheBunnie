#function for halting undecidable problem
def halt(x):
    if x == 0:
        return #code will stop if the user input is 0
    else:
        while True:
            pass #creates infinite loop whenever the user input is anything but 0

user_input = int(input("Enter a number: ")) #gets user input
halt(user_input) #calls function
