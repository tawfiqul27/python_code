#### Numeric built-in functions

x = '47'
y = int(x)
z = float(x)
# y = abs(x)        for absolute value
# y = divmod(x, 3)     for devision modulus value
# y = complex(x, 32)   this is for complex number. And will print 47 + 32j

### https://docs.python.org/3/library/functions.html
# this list all the built-in numeric functions.

print(x)
print(f'The type of x is {type(x)}')
print(y)
print(f'The type of y is {type(y)}')
print(z)
print(f'The type of z is {type(z)}')


### String functions

s = 'Hello world'
print(repr(s))      # repr is the best string representation function


class bunny:
    def __init__(self, n):
        self._n = n
    def __repr__(self):
        return f'repr: the number of bunnies is {self._n} 🖖'
    def __str__(self):
        return f'str: the number of bunnies is {self._n}'

p = bunny(47)
print(p)
print(repr(p))      # repr will pick repr method from the class bunny
print(ascii(p))     # this will print ascii value and unicode of any emoji
print(chr(128406))  # chr prints the character representation of that number
print(ord('🖖'))     # this will give you number of that character



###############################################################
##############################################################
# Container functions

k = (1, 2, 3, 4, 5)
# l = len(k)
# l = reversed(k)     # this will print reversed object string. 
# l = list(reversed(k))
# l = sum(k)      # there are max, min, any, all, 
l = (6, 7, 8, 9, 10)

z = zip(k, l)
print(k)
print(l)

for a, b in z:
    print(f'{a}   -   {b}')

print('------------This is the use of enumerator which set the index and value for a tupple-------------------')
c = ('cat', 'dog', 'raptile', 'eagle')

for i, v in enumerate(c): print(f'{i} - {v}')



# x = 42
# y = isinstance(x, int)         this will return true or false if x is not integer
# y = id(x)                      id will print the unique of variable x
# y = type(x)                    here type is a function and x is an object. These two combinely return the class of that object


