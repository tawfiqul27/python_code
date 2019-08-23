# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, 
# then tell them whether they guessed too low, too high, or exactly right. 
# (Hint: remember to use the user input lessons from the very first exercise)
# Extras:
#     Keep the game going until the user types “exit”
#     Keep track of how many guesses the user has taken, and when the game ends, print this out.



import random

a = random.randint(1, 9)
print('Generated random number is: {}'.format(a))



# b = input('Please get the input from an user: ')
# c = int(b)

def random_num():
    for x in range(1,10):
        b = input('Please enter a number between 1 to 9: ')
        c = int(b)
        if c == a:
            print("You got the number right. Bravo !!!!!")
            break
        elif (c-a) > 0:
            print('You entered a higher number')
        elif (c-a) < 0:
            print('You entered a lower number')
    print('Total number of attempts to guess the number: {}'.format(x))    


random_num()









