from typing import List

def maxProfit(prices: List[int]) -> int:
    left, right = 0, 1
    profit = 0

    while right < len(prices):
        if prices[left] >= prices[right]:
            left = right
            right +=1
        else:
            if (prices[right] - prices[left]) > profit:
                profit = prices[right] - prices[left]
                right +=1
            else:
                right +=1
    return profit

# print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([10,1,5,6,7,1]))
print(maxProfit([10,8,7,5,2]))