from typing import List

'''
1 0 2 0 0 7
3 1 0 1 3 8 9
0 0 9 4 0 0 3 8 0
'''

def move_zeros(nums: List[int]) -> None:
    # WRITE YOUR BRILLIANT CODE HERE
    left = 0s
    right = 0

    while right < len(nums):
        if nums[left] == 0 and nums[right] != 0:
            nums[left] = nums[right]
            nums[right] = 0
            left = right
            continue
        elif nums[left] != 0 and nums[right] == 0:
            left +=1
            right +=1
            continue
    return nums

if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    move_zeros(nums)
    print(' '.join(map(str, nums)))