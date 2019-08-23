# In this exercise, we will finish building Hangman. In the game of Hangman, the player only has 6 incorrect guesses (head, body, 2 legs, and 2 arms)
# before they lose the game. In Part 1, we loaded a random word list and picked a word from it. 
# In Part 2, we wrote the logic for guessing the letter and displaying that information to the user. 
# In this exercise, we have to put it all together and add logic for handling guesses.

# Copy your code from Parts 1 and 2 into a new file as a starting point. Now add the following features:
# Only let the user guess 6 times, and tell the user how many guesses they have left.
# Keep track of the letters the user guessed. If the user guesses a letter they already guessed, don’t penalize them - let them guess again.

# Optional additions:
# When the player wins or loses, let them start a new game.
# Rather than telling the user "You have 4 incorrect guesses left", display some picture art for the Hangman. This is challenging - do the other parts of the exercise first!


import random

f = open('/home/islamam/Desktop/python_scripts/Practice problem/sowpods.txt')
wordlist = []

def pick_word(a):
    for line in f:
        wordlist.append(line)
    g = random.sample(wordlist,a)
    p = list(g[0])
    del p[-1]
    print(p)
    word_length = len(p)
    q = 6 
    for i in range(word_length):
        for j in range(6):
            user_input = input('Enter the letter user want to guess: ')
            if user_input != p[i] and q > 0:
                print('Your guess is incorrect!!!')
                q = q - 1
                print("you have {} attempts left.".format(q))
            elif user_input == p[i] and q > 0:
                print("Your guess is correct.....!!!!")
                break
            print("you have total {} attempts left.".format(q))
        if q == 0:
            break
        
    return p 


print(pick_word(1))










