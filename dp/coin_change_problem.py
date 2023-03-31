# coins = [1,3,4, 5] amount = 7, Find least number of coins that make up the amount
# if we do greedily, [5,1,1] - > 3 coins
# but [3,4] is the correct answer
# can be figured out by backtracking + DFS (because we need to explore all possible combinations)
# But many subproblems are involved while drawing the choice map.
# so we memoize it with a DP array
# recursively it will take forever to finish

# Q1: Find least number of coins that can make up the amount.
# Q2: Find number of ways of making up the amount.


def num_ways_of_coins(denominations, n, way, ways):
    if n < 0:
        return
    if n == 0:
        ways.append(way)
    for i in range(len(denominations)):
        num_ways_of_coins(denominations[i:], n - denominations[i], way + [denominations[i]], ways)


def num_ways_of_coins_dp(dens, amount):
    coins = [0] * (amount + 1)
    coins[0] = 1
    for c in dens:
        for amt in range(1, amount + 1):
            if amt - c >= 0:
                coins[amt] += coins[amt - c]
    print(coins)
    return coins[amount]


def coin_change_ii(nums, target):
    ways = []
    num_ways_of_coins(nums, target, [], ways)
    num_ways_of_coins_dp(nums, target)
    print(ways)
    print(len(ways))


coin_change_ii([1, 2, 5], 7)


def least_num_coins_for_amt(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0  # number of coins required for making up amount=0

    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return dp[amount] if dp[amount] != amount + 1 else -1


# print(least_num_coins_for_amt([186, 419, 83, 408], 6249))