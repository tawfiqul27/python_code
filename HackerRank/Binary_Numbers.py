# Given a base-10 integer,n, convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum number of 
# consecutive 1's in n's binary representation.

# Input Format
# A single integer,n .

# Constraints:
# 1<=n<=10^6

# Output Format
# Print a single base-10 integer denoting the maximum number of consecutive 1's in the binary representation of n.

# Sample Input 1
# 5

# Sample Output 1
# 1

# Sample Input 2
# 13

# Sample Output 2
# 2


import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    b =[]
    while n>0:
        a = n%2
        b.append(a)
        n = n//2
    # print(b)
    b.reverse()
    # print(b)
    result= ''
    for element in b:
        result += str(element)

    # print(result)

# input.split('0') --> splits all sub-strings of  
# consecutive 1's separated by 0's, output will  
# be like ['11','1111'] 
# map(len,input.split('0'))  --> map function maps 
# len function on each sub-string of consecutive 1's 
# max() returns maximum element from a list 
    print (max(map(len, result.split('0')))) 




