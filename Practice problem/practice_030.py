# In this exercise, the task is to write a function that picks a random word from a list of words from the SOWPODS dictionary. 
# Download this file and save it in the same directory as your Python code.


import random

f = open('/home/islamam/Desktop/python_scripts/Practice problem/sowpods.txt')

wordlist = []

def pick_word(a):
    
    for line in f:
        wordlist.append(line)

    g = random.sample(wordlist,a)
    return g 


print(pick_word(1))











