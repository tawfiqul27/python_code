# For this exercise, we will keep track of when our friend’s birthdays are, and be able to find that information based on their name. 
# Create a dictionary (in your file) of names and birthdays. When you run your program it should ask the user to enter a name, and 
# return the birthday of that person back to them. The interaction should look something like this:

# >>> Welcome to the birthday dictionary. We know the birthdays of:
# Albert Einstein
# Benjamin Franklin
# Ada Lovelace
# >>> Who's birthday do you want to look up?
# Benjamin Franklin
# >>> Benjamin Franklin's birthday is 01/17/1706.


# birthday = {'Amin Mohammad':'09-02-1990', 'Mohammad Naimur':'01-01-1991'}

# # a = input("Who's birthday you want to look up?")
# # print(birthday['Amin Mohammad'])

# for a in birthday.keys():
#     b = input("Who's birthday you want to look up?\n")
#     if b == 'Amin Mohammad':
#         print(birthday.get['Amin Mohammad'])
#     elif b == 'Mohammad Naimur':
#         print(birthday.get['Mohammad Naimur'])
#     else:
#         print('You entered a worng name.')

birthdays = {
        'Albert Einstein': '03/14/1879',
        'Benjamin Franklin': '01/17/1706',
        'Ada Lovelace': '12/10/1815',
        'Donald Trump': '06/14/1946',
        'Rowan Atkinson': '01/6/1955'}

print('Welcome to the birthday dictionary. We know the birthdays of:')
for name in birthdays:
    print(name)

print('Who\'s birthday do you want to look up?')
name = input()
if name in birthdays:
    print('{}\'s birthday is {}.'.format(name, birthdays[name]))
else:
    print('Sadly, we don\'t have {}\'s birthday.'.format(name))













