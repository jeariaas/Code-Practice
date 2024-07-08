from typing import List

def two_sum_sorted(arr: List[int], target: int) -> List[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    left, right = 0, len(arr)-1
    
    while left < right:
        if arr[left] + arr[right] == target:
            return[left,right]
        elif arr[left] + arr[right] > target:
            right -=1
        else:
            left +=1
            
if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = two_sum_sorted(arr, target)
    print(' '.join(map(str, res)))