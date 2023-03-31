# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
def maxProfit(prices):
    n = len(prices)
    profits = []
    max_price = prices[-1]
    for i in range(n - 1, -1, -1):
        profits.append(max_price - prices[i])
        max_price = max(prices[i], max_price)
    return max(profits)


prices = [7, 1, 5, 3, 6, 4]
maxProfit(prices)

def max_profit(prices):
    n = len(prices)
    profit = []
    stack = []
    for i in range(n-1, -1, -1):
        if not stack:
            profit.append(-1)
            stack.append(prices[i])
        if prices[i] < stack[-1]:
            profit.append(stack[-1]-prices[i])
        else:
            profit.append(0)
            stack.pop()
            stack.append(prices[i])
    return profit[::-1]

print(max_profit(prices))