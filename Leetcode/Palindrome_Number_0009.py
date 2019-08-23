# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

# Example 1:
# Input: 121
# Output: true

# Example 2:
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# Example 4:
# Input: 0
# Output: True




# class Solution:
def isPalindrome(x):
    c = 0 
    c = x       # very important**** here c will hold the primary value of x. although, x will turn to 0 later on.

    if x < 0:
        print("False")
        return False
    if x == 0:
        print("True")
        return True
    if x > 0:
        a = []
        while x>0:
            b = x%10
            a.append(b)
            x = x//1
        print(a)
        res = (int("".join(map(str, a))))
        # print(res)
        # print(x)
    # print(c)
        if res == c:
            print("True")
            return True

isPalindrome(0)

# -> bool:


