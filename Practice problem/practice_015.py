# Write a program (using functions!) that asks the user for a long string containing multiple words. 
# Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
# My name is Michele

# Then I would see the string:
# Michele is name My

# shown back to me.


#### This is static programming without using function

# user_input = input()
# print(user_input)

# string_split = user_input.split()
# print(string_split)

# string_split.reverse()
# print(string_split)

# a = " "
# string_join = a.join(string_split)

# print(string_join)


#### Second way is to use of a function

def reverse_string(user_input):
    string_split = user_input.split()
    print(string_split)

    string_split.reverse()
    print(string_split)

    a = " "
    string_join = a.join(string_split)

    print(string_join)


a = input()
reverse_string(a)



