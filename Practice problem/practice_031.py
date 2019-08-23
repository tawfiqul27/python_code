# Let’s continue building Hangman. In the game of Hangman, a clue word is given by the program that the player has to guess, letter by letter. 
# The player guesses one letter at a time until the entire word has been guessed. 
# (In the actual game, the player can only guess 6 letters incorrectly before losing).
# Let’s say the word the player has to guess is “EVAPORATE”. For this exercise, write the logic that asks a player to guess a letter 
# and displays letters in the clue word that were guessed correctly. For now, let the player guess an infinite number of times until they get the entire word. 
# As a bonus, keep track of the letters the player guessed and display a different message if the player tries to guess that letter again. 
# Remember to stop the game when all the letters have been guessed correctly! Don’t worry about choosing a word randomly or 
# keeping track of the number of guesses the player has remaining - we will deal with those in a future exercise.

# An example interaction can look like this:
# >>> Welcome to Hangman!
# _ _ _ _ _ _ _ _ _
# >>> Guess your letter: S
# Incorrect!
# >>> Guess your letter: E
# E _ _ _ _ _ _ _ E
# ...

# And so on, until the player gets the word.


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
    for i in range(word_length):
        for j in range(26):
            user_input = input('Enter the letter user want to guess: ')
            if user_input != p[i]:
                print('Your guess is incorrect!!!')
            else:
                print("Your guess is correct.....!!!!")
                break
    return p 


print(pick_word(1))






