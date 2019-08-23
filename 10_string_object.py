print('1. Hello world'.upper())
print('2. Hello world'.swapcase())
print('3. Hello world'.lower())
print('4. Hello world'.capitalize())
print('5. Hello world'.title())
print('6. Hello world &'.casefold())     # its similar to lower but its more powerful

print('7. Hello world {}'.format(42 * 4))

s= '8. Hello world {}'
print(s.format(42 * 4))

g1 = 'Hello World. '
g2 = 'Can you join with me. '
g3 = '9. Please hold my hand.' ' Do not go far'

print(g3)
print(g1 + '  ' + g2)

class MyString(str):
    def __str__(self):
        return self[::-1]

p = MyString('Hello world')
print(s)

###########################################
###########################################
# Formatting string

a = 32
b = 33

print('11. The numbers are {xx} {yy}'.format(xx = a, yy=b))
print('12. The numbers are {0} {1}'.format(a, b))
print('13. The numbers are {0:<5} {1:<5}'.format(a, b))

l = a * b * 9200
print('14. The number with comma is {:,}'.format(l).replace(',','.'))
print('15. The number with comma is {:f}'.format(l))
print('16. The number with comma is {:.3f}'.format(l))
print('17. The number with comma is {:x}'.format(b))
print('18. The number with comma is {:o}'.format(b))
print(f'19. The number with comma is {a:b}')


##################################################
##################################################
# Splitting and joining

j = "20. This is for showing how splitting works."
k = j.split()

k2= '--'.join(k)

print(j.split())
print(j.split('i'))
print(k2)









