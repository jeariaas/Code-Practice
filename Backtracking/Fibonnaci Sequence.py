# def fib(n, memo):
#     if n in memo: # check in memo, if found, retrieve and return right away
#         return memo[n]
    
#     if n == 0 or n == 1:
#         return n
    
#     res = fib(n - 1, memo) + fib(n - 2, memo)
#     memo[n] = res # save in memo before returning
#     return res

# fib(3,[])

def fibonnaci(n):
    if n in memo:
        return memo[n]

    if n == 1 or n == 0:
        return n

    result = fibonnaci(n-1) + fibonnaci(n-2)
    memo[n] = result
    return result

memo = {}
print(fibonnaci(100))