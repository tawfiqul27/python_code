# Write a function to find the longest common prefix string amongst an array of strings.If there is no common prefix, return an empty string "".

# Example 1:
# Input: ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.



# class Solution:
def longestCommonPrefix(strs):
    # if strs[0] and strs[1]:
    #     strn= strs[0] and strs[1]
    a = len(strs)
    for i in range(1,len(strs)):
        
        strs[i]= strs[i] and strs[i-1]
# c = strn and strs[2]

        print(strs[i])
    return strs[a-1]
    # else:
    #     strn=""
    #     print('""')
    #     return strn

strs=["flower","flow","flight"]
longestCommonPrefix(strs)
# -> str:



