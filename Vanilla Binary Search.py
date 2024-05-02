from typing import List

#Code for Vanilla Binary Search - This code is dependent on the data being sorted. Otherwise wont work.
#Time complexity is O(log(n))

#Deducing Binary Search
#1. When to terminate the loop
#   Make sure the while lopp includes an equality comparion: otherwise, we might skip the loop and miss the potential match for the edhe of a one-element array
#2. Whether/how to update left and right boundary in the if condition
#   Consider which side to discard. If arr[mid] is smaller than the target, we shoudl discard everything on the left by making left = mid + 1
#3. Should i discard the current element?
#   For vanilla binary search, we can discard it since it cannot be the final answer if it is not equal to the target. There might be situations where you want to think twice before discarding the current element.
#When to use binary search
#   Binary search works beyond sorted arrays. You can use binary search whenever you make a binary decision to shrink the search range.

def binary_search(arr: List[int], target: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    left, right = 0, len(arr) -1
    while left <= right:
        mid = (left + right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid -1
    return -1

def example1():
    arr = [1,3,5,7,8]
    target = 5
    index = binary_search(arr, target)
    return index

def example2():
    arr = [1,2,3,4,5,6,7]
    target = 0
    index = binary_search(arr, target)
    return index

def example3():
    arr = [2,8,89,120,1000]
    target = 120
    index = binary_search(arr, target)
    return index

def example4():
    arr = [10,20]
    target = 20
    index = binary_search(arr, target)
    return index

if __name__ == '__main__':
    arr = [1,3,5,7,8]
    target = 5
    res = example1()
    print(res)
    res = example2()
    print(res)
    res = example3()
    print(res)
    res = example4()
    print(res)