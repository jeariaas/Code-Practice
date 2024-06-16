from typing import List


def hasDuplicate(nums: List[int]) -> bool:
         
    mySet = set()
    for number in nums:
        if number in mySet:
            return True
        mySet.add(number)
    return False



nums=[1,2,3,4]
print(hasDuplicate(nums))