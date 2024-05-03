def square_root(n: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    left, right = 0, n
    if n == 0:
        return 0
    boundary = -1
    while left <= right:
        mid = (left + right)//2
        if(mid*mid) == n:
            return mid
        elif(mid*mid) > n:
            boundary = mid
            right = mid -1
        else:
            left = mid + 1
    return boundary - 1

def example1():
    target = 4
    index = square_root(target)
    return index

def example2():
    target = 8
    index = square_root(target)
    return index

def example3():
    target = 10
    index = square_root(target)
    return index

def example4():
    target = 0
    index = square_root(target)
    return index

def example5():
    target = 1
    index = square_root(target)
    return index

def example6():
    target = 8
    index = square_root(target)
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