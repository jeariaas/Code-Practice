from typing import List
from math import inf

# def dfs(coins, amount, sum):
#         if sum == amount:
#             return 0
#         if sum > amount:
#             return inf
        
#         ans = inf
#         for coin in coins:
#             result = dfs(coins, amount, sum+coin)
#             if result == inf:
#                 continue
#             ans = min(ans, result+1)

#         return ans


def dfs(coins, amount, sum):
    
    if amount == 0: 
        result = sum
        return result
    
    if not coins:
        return inf
    
    while amount - coins[0] >= 0:
        amount = amount - coins[0]
        sum +=1
    coins.remove(coins[0])
    result = max(sum, dfs(coins, amount, sum))

def coin_change(coins: List[int], amount: int) -> int:
    coins.sort(reverse = True)
    result = dfs(coins, amount, 0)
    return result if result != inf else -1


if __name__ == '__main__':
    coins = [int(x) for x in input().split()]
    amount = int(input())
    res = coin_change(coins, amount)
    print(res)
