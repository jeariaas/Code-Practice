from typing import List
from heapq import heappush, heappop, heapify

def find_kth_largest(nums: List[int], k: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE

    nums = [-x for x in nums]
    heapify(nums)
    for i in range(k-1):
        heappop(nums)
    return -nums[0]

if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    k = int(input())
    res = find_kth_largest(nums, k)
    print(res)

    '''
    input =
    3 2 1 5 6 4
    2

    3 2 3 1 2 4 5 5 6
    4

    5 7 2 1 3 9 6 7 6
    7
    '''