# we’ve written a program that “knows” a number and asks a user to guess it.

# This time, we’re going to do exactly the opposite. You, the user, will have in your head a number between 0 and 100. The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.

# At the end of this exchange, your program should print out how many guesses it took to get your number.


import random

a = eval(input("User will input a number between 0 to 100: ")) 

def program_guess():
    for i in range(0,101):
        b = random.randint(0,100)
        if b == a:
            print("This program guess the number right.")
            break
        elif b<a:
            print("This program guess higher number.")
        else:
            print("This program guess lower number.")
    print("Total number of iteration: {}".format((i+1)))
    return (i+1)


d = program_guess()
print(d)
# print("Total number of iteration: {}".format((i+1)))



