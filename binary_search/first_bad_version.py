# https://leetcode.com/problems/first-bad-version/
def isBadVersion(n):
    if n == 4:
        return True
    else:
        return False


# if false, check the future versions
# if true, check the older versions and find the least
def bad_version(n):
    arr = [i for i in range(1, n + 1)]
    l = 0
    r = n - 1
    while l < r:
        mid = (l + r) // 2
        if isBadVersion(arr[mid]):
            r = mid
        else:
            l = mid+1

    return arr[l]

print(bad_version(n=5))