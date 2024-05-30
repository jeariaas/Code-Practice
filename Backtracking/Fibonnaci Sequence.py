def fib(n, memo):
    if n in memo: # check in memo, if found, retrieve and return right away
        return memo[n]
    
    if n == 0 or n == 1:
        return n
    
    res = fib(n - 1, memo) + fib(n - 2, memo)
    memo[n] = res # save in memo before returning
    return res

fib(3,[])