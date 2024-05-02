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
    return 0

def example1():
    arr = [False, False, False, True, True, True]
    target = True
    index = find_boundary(arr, target)
    return index

def example2():
    arr = [False, False, False, False, False]
    target = 0
    index = find_boundary(arr, target)
    return index

def example3():
    arr = [True, True, True, True, True]
    target = 120
    index = find_boundary(arr, target)
    return index

def example4():
    arr = [10,20]
    target = 20
    index = find_boundary(arr, target)
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