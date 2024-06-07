from typing import List

#backtracking template
#
# - Check when to finish depth of a branch reaching max case or all its children are null - In this case its when the start index reaches input size of 2 ex 'aa' = 2
#
# Looping - some kind of for loop that iterates through the tree. Using recursion it gets the root -> child -> child child until it reaches its end where either its child is null
# Cleaning the stack - after the recursion there is a .pop() to remove everything from the stack.


def letter_combination(n):
    if n == 0:
        return ''
    def dfs(start_index, path):
        if start_index == n:
            result.append(''.join(path))
            return
        
        letters = ['a', 'b']
        for letter in letters:
            path.append(letter)
            dfs(start_index+1, path)
            path.pop()
    
    result = []
    dfs(0, [])
    return result


if __name__ == '__main__':
    n = int(input())
    res = letter_combination(n)
    for line in sorted(res):
        print(line)