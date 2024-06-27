# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:
# Input: strs = ["act","pots","tops","cat","stop","hat"]
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

# Example 2:
# Input: strs = ["x"]
# Output: [["x"]]

# Example 3:
# Input: strs = [""]
# Output: [[""]]

from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    
    ans = {}
    temp = {}
    for word in strs:
        for letter in word:
            # print(letter)
            if letter in temp:
                temp[letter] +=1
            else:
                temp.update({letter : 1})
        ans.update({word: temp.copy()})
        temp.clear()
    # print(ans)
    answer = []
    temporary = []
    for example, map in ans.items():
        for example2, map2 in ans.items():
            if map == map2:
                temporary.append(example)
        answer.append(temporary.copy())
        temporary.clear()    
    print(answer)
    


    
    return



groupAnagrams(["act","pots","tops","cat","stop","hat"])