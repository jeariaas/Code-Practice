from typing import List

def partition(s: str) -> List[List[str]]: #Returns a list of list of strings
    # WRITE YOUR BRILLIANT CODE HERE

    def dfs(start_index, path):
        #need to find the condition that the loop finishes. this case its the start index equaling the length of the string
        if start_index == len(s):
            result.append(path)
            return
        
    def ispalindrome(string) -> bool:
        start, end = 0, len(string) - 1
        if len(string) == 1 or len(string) == 0:
            return True
        while start < end:
            if string[start] == string[end]:
                start+=1
                end-=1
            else:
                return False
        return True

    result = []
    ispalindrome(s)
    dfs(0, [])
    return []
    

if __name__ == '__main__':
    s = input()
    res = partition(s)
    for row in res:
        print(' '.join(row))
