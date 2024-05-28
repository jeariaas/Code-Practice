from typing import List

def partition(s: str) -> List[List[str]]:
    # WRITE YOUR BRILLIANT CODE HERE
    
    end_cond = len(s)
    
    def isPalindrome(string: str) -> bool:
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
        
    
    def dfs(start_index: int, current_path: list):
        
        if start_index == end_cond:
            result.append(current_path)
            return
        for end in range(start_index + 1, end_cond + 1):
            prefix = s[start_index: end]
            if isPalindrome(prefix):
                dfs(end, current_path + [prefix])
    
    result = []
    dfs(0,[])
    return result

if __name__ == '__main__':
    s = input()
    res = partition(s)
    for row in res:
        print(' '.join(row))
