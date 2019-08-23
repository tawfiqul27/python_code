# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 
# Hint: how does an even / odd number react differently when divided by 2?

a = input('Please enter the a number from the keyboard: ')
b = int(a)
c = b%2

if c == 0:
    print('The number is an even number. ')
else:
    print('The number is an odd number. ')


