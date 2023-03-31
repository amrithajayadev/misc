def square_root(x):
    r = x // 2
    l = 1
    sqrt = -1
    while l <= r:
        mid = (l + r) // 2
        if mid * mid == x:
            return mid
        if mid * mid < x:
            sqrt = mid
            l = mid + 1
        else:
            r = mid - 1
    return sqrt

#Given an integer x, find it’s square root. If x is not a perfect square, then return floor(√x).
# square root of 11 lies between 3 and 4.
print(square_root(4))
