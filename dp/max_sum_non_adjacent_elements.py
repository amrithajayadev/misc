# arr = [75, 105, 120, 75, 90, 135]
# arr = [5, 5, 10, 100, 10, 5]
# arr = [3, 2, 7, 10]
# arr = [3, 2, 5, 10, 7]
arr = [1]


def solve(arr, i, n):
    if i > n:
        return 0
    if i == n-1:
        return arr[i]
    return max(arr[i] + solve(arr, i + 2, n), solve(arr, i + 1, n))


print(solve(arr, 0, len(arr)-1))

t = [-1] * (len(arr) - 1)


def solve_dp(arr, i, n, t):
    if i > n:
        return 0
    if i == n:
        return arr[n]
    if t[i] != -1:
        return t[i]
    t[i] = max(arr[i] + solve(arr, i + 2, n), solve(arr, i + 1, n))
    return t[i]


print(solve_dp(arr, 0, len(arr) - 1, t))
