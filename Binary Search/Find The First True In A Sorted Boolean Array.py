# Explanation

# The binary decision we must make when we look at an element is:

#     If the element is false, we discard everything to the left and the current element itself.
#     If the element is true, the current element could be the first true although there may be other true to the left. We discard everything to the right but what about the current element?

# We can either keep the current element in the range or record it somewhere and then discard it. Here we choose the latter. 
# We'll discuss the other approach in the alternative solution section.

# We keep a variable boundary_index that represents the currently recorded leftmost true's index. 
# If the current element is true, then we update boundary_index with its index and discard everything to the right including the current element itself since its index has been recorded by the variable.

from typing import List

def find_boundary(arr: List[bool]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    left, right = 0, len(arr) -1
    boundary = -1

    while left <= right:
        mid = (left + right)//2
        if arr[mid]:
            boundary = mid
            right = mid - 1
        else:
            left = mid + 1
    return boundary

def alternate_find_bundary(arr: List[bool]) -> int: #This could keeps track of the current element in the search range and doesnt discard it. However it has a modified leave case, as to not induce a forever while loop
    # WRITE YOUR BRILLIANT CODE HERE
    left, right = 0, len(arr) -1
    boundary = -1

    while left < right:
        mid = (left + right)//2
        if arr[mid]:
            boundary = mid
            right = mid
        else:
            left = mid + 1

    return boundary

def example1():
    arr = [False, False, False, True, True, True]
    # index = find_boundary(arr)
    index = alternate_find_bundary(arr)
    return index

def example2():
    arr = [False, False, False, False, False]
    # index = find_boundary(arr)
    index = alternate_find_bundary(arr)
    return index

def example3():
    arr = [True, True, True, True, True]
    # index = find_boundary(arr)
    index = alternate_find_bundary(arr)
    return index

def example4():
    arr = [False]
    # index = find_boundary(arr)
    index = alternate_find_bundary(arr)
    return index

def example5():
    arr = [True]
    # index = find_boundary(arr)
    index = alternate_find_bundary(arr)
    return index

def example6():
    arr = []
    # index = find_boundary(arr)
    index = alternate_find_bundary(arr)
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