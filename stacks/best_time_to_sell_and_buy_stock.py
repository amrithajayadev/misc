# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

def find_max_profit(prices):
    max_profit = 0
    for i in range(len(prices) - 1):
        profit = max(prices[i + 1] - prices[i], 0)
        max_profit += profit
    print(max_profit)


find_max_profit([7, 1, 5, 3, 6, 4])