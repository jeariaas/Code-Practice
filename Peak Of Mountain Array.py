from typing import List

#A mountain array is defined as an array that:
#   1. Has at least three elements
#   2. Has an element with the largest value called peak, with index k. The array elements strictly increase from the first element to A[k], 
#       and then strictly decrease from A[k+1] to the last element of the array.
#Need to find a limiting binary decider. If A[i] < A[i+1]
#[1,2,3,4,3,2,1,0] => A[1,2,3,4,3,2,1,0] = [True,True,True,False,False,False,False,False], [True,True,True,True,True,False,False,False]
#Thus turns into a first false binary search 


def peak_of_mountain_array(arr: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE   
    if len(arr) < 3:
        return -1

    left, right = 0, len(arr)-1
    peak = -1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] < arr[mid+1]:
            peak = mid + 1
            left = mid + 1
        else:
            right = mid - 1
    return peak

def example1():
    arr = [0,1,2,3,2,1,0]
    index = peak_of_mountain_array(arr)
    return index

def example2():
    arr = [0,10,3,2,1,0]

    index = peak_of_mountain_array(arr)
    return index

def example3():
    arr = [0,10,0]

    index = peak_of_mountain_array(arr)
    return index

def example4():
    arr = [0, 1, 2, 12, 22, 32, 42, 52, 62, 72, 82, 92, 102, 112, 122, 132, 133, 132, 111, 0]

    index = peak_of_mountain_array(arr)
    return index

def example5():
    arr = [0, 10]
    index = peak_of_mountain_array(arr)
    return index

def example6():
    arr = []

    index = peak_of_mountain_array(arr)
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