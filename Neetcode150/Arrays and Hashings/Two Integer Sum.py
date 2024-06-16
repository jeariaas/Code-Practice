# Two Integer Sum
# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
# Return the answer with the smaller index first.

# Example 1:
# Input: 
# nums = [3,4,5,6], target = 7
# Output: [0,1]
# Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

# Example 2:
# Input: nums = [4,5,6], target = 10
# Output: [0,2]

# Example 3:
# Input: nums = [5,5], target = 10
# Output: [0,1]

# Constraints:
#     2 <= nums.length <= 1000
#     -10,000,000 <= nums[i] <= 10,000,000
#     -10,000,000 <= target <= 10,000,000

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    left , right = 0, len(nums) -1
    nums.sort()

    while left <= right:
        if nums[left] + nums[right] == target:
            return list([nums[left], nums[right]])
        elif nums[left] + nums[right] < target:
            left = left + 1
        else:
            right = right - 1

nums = [-1,-2,-3,-4,-5]
target = -6
print(twoSum(nums, target))