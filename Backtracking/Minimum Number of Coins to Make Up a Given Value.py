from typing import List

def coin_change(coins: List[int], amount: int) -> int:
    coins.sort(reverse=True)

    def dfs(ways, remains):

        if remains == 0:
            result[0]
            return ways

        for number in coins:
            if remains - number >= 0:
        return

    result = []
    dfs(0, amount)
    return result
if __name__ == '__main__':
    coins = [int(x) for x in input().split()]
    amount = int(input())
    res = coin_change(coins, amount)
    print(res)
