x = "abcdgh"
y = "abedfhr"


def lcs(x, y, n, m):
    if n == 0 or m == 0:
        return 0
    if x[n - 1] == y[m - 1]:
        return lcs(x, y, n - 1, m - 1) + 1
    else:
        return max(lcs(x, y, n - 1, m), lcs(x, y, n, m - 1))


# print(lcs(x, y, len(x), len(y)))

memo = [[-1 * (1000 + 1)] * (1000 + 1)]


def lcs_memoize(x, y, n, m):
    if n == 0 or m == 0:
        return 0
    if memo[n][m] != -1:
        return memo[n][m]
    if x[n - 1] == y[m - 1]:
        memo[n][m] = lcs(x, y, n - 1, m - 1) + 1
        return memo[n][m]
    else:
        memo[n][m] = max(lcs(x, y, n - 1, m), lcs(x, y, n, m - 1))
        return memo[n][m]


# print(lcs_memoize(x, y, len(x), len(y)))

def lcs_dp(s1, s2):
    dp = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    for i in range(len(s1)+1):
        print(dp[i])
    return dp[-1][-1]

lcs_dp("abcde", "ace")