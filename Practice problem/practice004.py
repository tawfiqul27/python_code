# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number. 
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)




a = input('Please enter a number to get its divisor: ')
b = int(a)
c = []

def num():
    for number in range(1,1000):
        if (b%number) == 0:
            c.append(number)
        else:
            pass

num()
print("The list of the divisor of number {} is: ".format(b))
print(c)


# this is another way of solving this problem

# for number in range(1,1000):
#     if (b%number) == 0:
#         c.append(number)
#         print(c)
#     else:
#         pass
    















