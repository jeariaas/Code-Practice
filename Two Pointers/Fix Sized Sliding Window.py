from typing import List

def subarray_sum_fixed(nums: List[int], k: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    sum = 0
    left, right = 0, k

    while right < len(nums):
        temp= 0
        for x in range(left,right):
            temp += nums[x]
        if temp > sum:
            sum = temp
        right +=1
        left +=1
    return sum

if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    k = int(input())
    res = subarray_sum_fixed(nums, k)
    print(res)