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

56
def letter_combinations_of_phone_number(digits: str) -> List[str]: #need to return a list of the combinations like ['adg', 'beh', 'xxx', etc]

    def dfs(start_index: int, path: List[str]):

        #need to create the function/if statement that will equal a condition therefore we know we reached the end of the first loop. This function will create the output on the result variable of what we want
        # print(len(digits))
        if start_index == len(digits): #star_index == len(digits) because we know we need it to add len(digits) amount of numbers to the combination
            result.append(''.join(path))
            return
        
        #need to create the function that iterates through the digits and then does a recursive combination.
        current_number = digits[start_index]
        for letter in KEYBOARD[current_number]: #takes the 
            path.append(letter)
            # print(path)
            dfs(start_index + 1, path)
            path.pop()

    result = [] #this is the list that the return will be in
    dfs(0, []) #creating the recursion function which is a dfs. Using the input variables of start_index and path
                           #Using start_index 0, because: thats how we will keep count that we have n # of letters per combination. n is dictated by the user input
                           #Using path [] because: so we can keep track of what current letters we have added. Essentially the path is a stack and will be popped out when finish a loop of recursion
    return result
    



if __name__ == '__main__':
    digits = input()
    res = letter_combinations_of_phone_number(digits)
    print(' '.join(res))