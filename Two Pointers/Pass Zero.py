from typing import List

'''
1 0 2 0 0 7
3 1 0 1 3 8 9
0 0 9 4 0 0 3 8 0
'''

def move_zeros(nums: List[int]) -> None:
    # WRITE YOUR BRILLIANT CODE HERE
    # slow = 0
    # for fast in range(len(nums)):
    #     if nums[fast] != 0:
    #         nums[slow], nums[fast] = nums[fast], nums[slow]
    #         slow += 1
    # return nums

    slow = 0
    
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            nums[fast] = nums[slow]
            slow +=1
    return nums

if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    move_zeros(nums)
    print(' '.join(map(str, nums)))