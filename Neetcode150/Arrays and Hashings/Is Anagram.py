# Is Anagram
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:
# Input: s = "racecar", t = "carrace"
# Output: true

# Example 2:
# Input: s = "jar", t = "jam"
# Output: false
# Constraints:
# s and t consist of lowercase English letters.

def isAnagram(s: str, t: str) -> bool:
    word1 = dict()
    word2 = dict()

    for letter in s:
        if letter not in word1:
            word1.update({letter: 1})
        else:
            word1[letter]+=1

    for letter in t:
        if letter not in word2:
            word2.update({letter: 1})
        else:
            word2[letter]+=1
    if word1 == word2:
        return True
    else:
        return False

s = "jam"
t = "jar"
isAnagram(s,t)
