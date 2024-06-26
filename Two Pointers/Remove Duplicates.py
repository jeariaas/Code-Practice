from typing import List

'''
0 0 1 1 1 2 2
'''

def remove_duplicates(arr: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    
    pointer1 = 0
    pointer2 = 0
    
    while pointer2 < len(arr):
        if arr[pointer1] == arr[pointer2]:
            pointer2 +=1
        else:
            pointer1 +=1
            arr[pointer1] = arr[pointer2]
    return arr

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    res = remove_duplicates(arr)
    print(' '.join(map(str, arr[:res])))