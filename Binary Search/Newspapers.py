from typing import List

def feasable(newspapers_read_times: List[int], num_coworkers: int, limit: int):
    time, num_workers = 0, 0
    for read_time in newspapers_read_times:
        if time + read_time > limit:
            time = 0
            num_workers +=1
        time +=read_time
    if time != 0:
        num_workers +=1
    
    return num_workers <= num_coworkers

def newspapers_split(newspapers_read_times: List[int], num_coworkers: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE

    low, high = max(newspapers_read_times), sum(newspapers_read_times)
    ans = -1

    while low <= high:
        mid = (low + high)//2
        if (feasable(newspapers_read_times, num_coworkers, mid)):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans

def example1():
    arr = [7,2,5,10,8]
    num = 2
    index = newspapers_split(arr, num)
    return index

def example2():
    arr = [1,4,4]
    num = 3
    index = newspapers_split(arr, num)
    return index

def example3():
    arr = [2873, 2837, 10, 3, 12, 34, 21, 450, 12, 4, 39, 1, 40, 59, 2, 67, 93, 49, 837, 499, 237, 287, 459, 12309, 9249, 94878, 30]
    num = 4
    index = newspapers_split(arr, num)
    return index

def example4():
    arr = [1,1,1,1,1,1]
    num = 6
    index = newspapers_split(arr, num)
    return index

def example5():
    arr = [15,15,15,15]
    num = 4
    index = newspapers_split(arr, num)
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