# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and
# makes a new list of only the first and last elements of the given list.
# For practice, write this code inside a function.

print('Keep on adding the number to the list. Press e to end of adding number to the list.')

a =[]

def number():
    for num in range(1,1001):
        b = input()
        if b == 'e':
            break
        else:
            c = int(b)
            a.append(c)
    


number()
print(a)

d = a[0]
e = a[-1]

print('The first and last number in the list are {} and {}'.format(d,e))














