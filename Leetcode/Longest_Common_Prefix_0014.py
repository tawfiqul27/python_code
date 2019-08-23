# Write a function to find the longest common prefix string amongst an array of strings.If there is no common prefix, return an empty string "".

# Example 1:
# Input: ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Solution

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs: 
        print('""')
        return ""
    if len(strs) == 1: 
        print(strs[0])
        return strs[0]
    
    strs.sort()
    p = ""
    for x, y in zip(strs[0], strs[-1]):
        if x == y: p+=x
        else: break
    print(p)
    return p
# strs=["dog","racecar","car"]
strs=["flower","flow","flight"]
longestCommonPrefix(strs)

# -> str:




