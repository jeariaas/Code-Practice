def decode_ways(digits: str) -> int:
    # WRITE YOUR BRILLIANT CODE HERE

    decode = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
    'K': 10,
    'L': 11,
    'M': 12,
    'N': 13,
    'O': 14,
    'P': 15,
    'Q': 16,
    'R': 17,
    'S': 18,
    'T': 19,
    'U': 20,
    'V': 21,
    'W': 22,
    'X': 23,
    'Y': 24,
    'Z': 25
}

    def dfs(start_index):
        if start_index == len(str(digits)):
            return ans
        
        ans = start_index
        
        for number in 
        

    
    ans = 0
    dfs(0)
    return ans

if __name__ == '__main__':
    # digits = input()
    digits = 123
    res = decode_ways(digits)
    print(res)