from typing import List

#Time complexity O(log(N))
#Space complexity O(1)

def first_not_smaller(arr: List[int], target: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    left, right = 0, len(arr) -1
    boundary = -1

    while left <= right:
        mid = (left + right)//2
        if arr[mid] == target:
            boundary = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return boundary

def example1():
    arr = [1, 3, 3, 3, 3, 3, 3, 5, 8, 8, 10]
    target = 3
    index = first_not_smaller(arr, target)
    return index

def example2():
    arr = [0]
    target = 0
    index = first_not_smaller(arr, target)
    return index

def example3():
    arr = [1,2,3,4,5,6,7,8,9,10]
    target = 10
    index = first_not_smaller(arr, target)
    return index

def example4():
    arr = [2,3,5,7,11]
    target = 2
    index = first_not_smaller(arr, target)
    return index

def example5():
    arr = [86, 124, 232, 371, 422, 443, 696, 1189, 1306, 1517, 1718, 1730, 1908, 2119, 2368, 2449, 2578, 2827, 2997, 3116, 3349, 3488, 3620, 3801, 3861, 4171, 4288, 4498, 4673, 4711, 4726, 4774]
    target = 3844

    index = first_not_smaller(arr, target)
    return index

def example6():
    arr = []
    target = 2
    index = first_not_smaller(arr, target)
    return index

if __name__ == '__main__':
    res = example1()
    print(res)
    res = example2()
    print(res)
    res = example3()
    print(res)
    res = example4()
    print(res)
    res = example5()
    print(res)
    res = example6()
    print(res)