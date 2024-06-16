from typing import List

def word_break(target, words):
    def dfs(start_index):
        if start_index == len(target):
            return True
        
        ans = False
        for word in words:
            if target[start_index:].startswith(word):
                ans = ans or dfs(start_index + len(word))
        
        return ans
    
    return dfs(0)

#Need to check if the words list appear in the first 

if __name__ == '__main__':
    s = input()
    words = input().split()
    res = word_break(s, words)
    print('true' if res else 'false')
