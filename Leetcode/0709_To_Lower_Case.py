# Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

# Example 1:
# Input: "Hello"
# Output: "hello"

# Example 2:
# Input: "here"
# Output: "here"

# Example 3:
# Input: "LOVELY"
# Output: "lovely"


def toLowerCase(str):
    b=''
    for a in str:
        b+=(a.lower())
    print(b)
    return b

c = "amin"
toLowerCase(c)