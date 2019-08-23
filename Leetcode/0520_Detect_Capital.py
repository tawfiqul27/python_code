# Given a word, you need to judge whether the usage of capitals in it is right or not. We define the usage of capitals in a word to be right when one of the following cases holds:
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".

# Otherwise, we define that this word doesn't use capitals in a right way.

# Example 1:
# Input: "USA"
# Output: True

# Example 2:
# Input: "FlaG"
# Output: False


def detectCapitalUse(word):
    if word.isupper() == True:
        print("True")
        return True
    if word.islower() == True:
        print("True")
        return True
    a =''
    if word[0].isupper() == True and word[1].islower() == True:
        if len(word) == 2:
            return True
        else:
            for i in range(2,len(word)):
                if word[i].isupper() == True:
                    print("False")
                    return False
                    break
                elif word[i].islower() == True:
                    a += word[i].lower()
            if a.islower() == True:
                print("True")
                return True


word = 'GeeKs'
detectCapitalUse(word)


# -> bool:







