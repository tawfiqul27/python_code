# Easy mode: Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321

# Example 2:

# Input: -123
# Output: -321

# Example 3:

# Input: 120
# Output: 21

# Input: 1534236469
# Output: 0

## Important learning: don't return anything inside if..else condition. 


class Solution:
    def reverse(self, x):
        a = []
        if x > 0:
            while x>0:
                b = x%10
                a.append(b)
                x = x//10
            print(a) 
            res = int("".join(map(str, a))) ### this join list of interger to a single integer
            if res > ((2**31)-1):
                res = 0
                print(res)
            else:
                print(res)
            print(res)
            return res
    
        elif x==0:
            print(x)
            return x

        else:
            x = abs(x)
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
            return res


reverse(-123)













