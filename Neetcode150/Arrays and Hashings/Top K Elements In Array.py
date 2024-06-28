


from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    map = {}
    for numbers in nums:
        print(numbers)
        if numbers not in map:
            map.update({numbers: 1})
        else:
            map[numbers] +=1
    print(map)
    answer = [0] * k
    for index, value in map.items():
        
    return


topKFrequent(nums = [1,2,2,3,3,3], k = 2)