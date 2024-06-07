from typing import List


KEYBOARD = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}

def letter_combinations_of_phone_number(digits: str) -> List[str]: #need to return a list of the combinations like ['adg', 'beh', 'xxx', etc]
    
    def dfs(start_index, path):
        if start_index == len(str(digits)):
            result.append(''.join(path))
            return
        
        letters = KEYBOARD[digits[start_index]]
        for digit in letters:

            path.append(digit)
            dfs(start_index + 1, path)
            path.pop()
    
    result =[]
    dfs(0, [])
    return result
    



if __name__ == '__main__':
    digits = input()
    res = letter_combinations_of_phone_number(digits)
    print(' '.join(res))