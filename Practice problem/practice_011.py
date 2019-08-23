# Ask the user for a number and determine whether the number is prime or not.


a = input('Please enter a number to check if its a prime number or not: ')
b = int(a)
c = []


def num():
    for number in range(1,1000):
        if (b%number) == 0:
            print('b is not a prime number. ')
            break
        else:
            print('b is a prime number. ')

num()
# print("The list of the divisor of number {} is: ".format(b))
# print(c)











