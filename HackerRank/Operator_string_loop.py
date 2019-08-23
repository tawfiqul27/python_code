# Task
# Given a string, S, of length N that is indexed from 0 to N-1, print its even-indexed and odd-indexed 
# characters as 2 space-separated strings on a single line (see the Sample below for more detail).

# Note: 0 is considered to be an even index.

# Input Format
# The first line contains an integer, T (the number of test cases). Each line i of the T subsequent lines contain a String, S.

# Constraints:
# 1<=T<=10
# 2<=length of S <= 10000

# Output Format
# For each String Sj(where 0<=j<=T-1), print Sj's even-indexed characters, followed by a space, followed by Sj's odd-indexed characters. 

# Sample Input:
# 2
# Hacker
# Rank

# Sample Output:
# Hce akr
# Rn ak

T = int(input())        # Number of test cases 
if 1<=T<=10:
    for i in range(0,T):
        S = str(input())        # input the String
        if 2<=len(S)<=10000:
            for p in range(0,len(S)):
                if p%2 == 0:
                    print(S[p],end="")
            print(end=" ")
            for q in range(0,len(S)):
                if q%2 != 0:
                    print(S[q],end="")
            print(end="\n")





