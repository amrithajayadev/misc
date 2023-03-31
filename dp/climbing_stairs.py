# recursion
import time


def climbing_stairs(n):
    if n < 0:
        return 0
    if n == 1 or n == 0:
        return 1
    return climbing_stairs(n - 1) + climbing_stairs(n - 2)

st = time.time()
print(climbing_stairs(35))
et = time.time()
print(f"climbing_stairs took {et-st} secs")


def climbing_stairs_dp(n, memo):
    for i in range(2,n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]

n = 35
memo = [-1]*(n+1)
memo[0] = 1
memo[1] = 1

st = time.time()
print(climbing_stairs_dp(n, memo))
et = time.time()
print(f"climbing_stairs_memoize took {et-st} secs")