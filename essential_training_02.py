# to print the type of an integer

# x = 7 
# x = 7.0
# x = '7.0'
# x = True
# x = None
# x = 'seven'.capitalize()
# x = 'seven'.upper()
# x = 'SEVEN'.lower()
# x = 'seven {} {}'.format(8, 9)
# x = 'seven {1} {0}'.format(8, 9)
# x = 'seven {1:<9} {0:>9}'.format(8, 9)      # this will put 9 spaces on right of 9 and put 9 spaces on left of 8

from decimal import *

a = 8
b = 9
x = f'seven {a} {b}'

print('X value is {}'.format(x))
print(type(x))          # type is a keyword


### To work floating point module you have to be very careful. Floating point number
# has precision but doesn't have accuracy

p = Decimal('.10')
q = Decimal('.30')
# r = p + p + p - q
r = p + p + p + p - q       # this is for next true or false program
print('r value is {}'.format(r))
print(type(r))

if r:
    print('True')
else:
    print('False')



# working with Tuple and list 

g = [1, 2, 3, 4, 5, 6]      # this is a list
h = (1, 2, 3, 4, 5, 6)      # this is a tuple. The difference of tupple is you cannot change the value of tuple

# g[3] = 34
# g = range(5)
# g = range(5, 10) 
# g = range(5, 45, 5)   increase by 5


# g = list(range(5))
# g [2] = 323       range works as tuple and the value cannot be changed unless you define it using a the list constructor


for i in h:
    print('i value is {}'.format(i))
print(type(h))
print(id(h))            # id function returns the unique identifier number of an object
print(id(h[3]))         # this will print the object number of element three

l = {'one': 1, 'two': 2, 'three': 3, 'four': 4}   # this is a ictrionary which is defined by key value pair

l ['three'] = 53
for k, v in l.items():
    print('k: {}, v: {}'.format(k, v))

print(type(l))
print(id(l))


if g is h:          # use of is command
    print('g and h are the same')
else:
    print('g and h are not the same')


if isinstance(g, tuple):    # use of isinstance. this is an comparison command
    print('g is a tuple')
else:
    print('g is not a tuple')
    







