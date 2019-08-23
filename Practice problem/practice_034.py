# In the previous exercise we created a dictionary of famous scientists’ birthdays. In this exercise, modify your program from Part 1 to load 
# the birthday dictionary from a JSON file on disk, rather than having the dictionary defined in the program.

# Bonus: Ask the user for another scientist’s name and birthday to add to the dictionary, and update the JSON file you have on disk 
# with the scientist’s name. If you run the program multiple times and keep adding new names, your JSON file should keep getting bigger and bigger.


import json

filename = '/home/islamam/Desktop/python_scripts/Practice problem/birthday.json'

with open(filename) as new_file:
    birthday = json.load(new_file)

print(birthday)



# print('Welcome to the birthday dictionary. We know the birthdays of:')
# for name in birthdays:
#     print(name)

# print('Who\'s birthday do you want to look up?')
# name = input()
# if name in birthdays:
#     print('{}\'s birthday is {}.'.format(name, birthdays[name]))
# else:
#     print('Sadly, we don\'t have {}\'s birthday.'.format(name))


