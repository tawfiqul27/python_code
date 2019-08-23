# from array import *


# arrayName = array(typecode, [Initializers])  b,c,i,f for byte, character, integer, floating 



x= -1534236469
x = abs(x)
a=[]
while x>0:
    b = x%10
    a.append(b)
    x = x//10
print(a) 
res = (int("".join(map(str, a))))
if res > (2**31):
    res = 0
    print(res)
else:
    print(res)
res = res*(-1) 
print(res)




