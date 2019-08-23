# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

# Example:

# Input: 38
# Output: 2 
# Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
#             Since 2 has only one digit, return it.

def addDigits(num): 
    b= list(str(num))
    if len(b) == 1:
        print(num)
        return num
    else:
        c = 0
        for i in range(len(b)):
            c = c + int(b[i])
        if len(list(str(c))) == 1:
            print(c)
            return c
        else:
            d = list(str(c))
            e = 0
            for j in range(len(d)):
                e = e + int(d[j])
            if len(list(str(e))) == 1:
                print(e)
                return e
            else:
                f = list(str(e))
                g = 0
                for k in range(len(f)):
                    g = g + int(f[k])
                if len(list(str(g))) == 1:
                    print(g)
                    return g


addDigits(199)

# -> int:











