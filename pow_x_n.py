def myPow(x: float, n: int) -> float:
    if x == 0:
        return 0
    if n == 0:
        return 1

    if n > 0:
        return x * myPow(x, n - 1)
    if n < 0:
        return 1 / x * myPow(x, (n + 1))


# print(myPow(2.100, 3))
# print(myPow(2.000, -2))
#

# above code runs into max recursion depth so memoize

def myPow2(x: float, n: int) -> float:
    dict_pow = {}
    if x == 0:
        return 0
    if n == 0:
        return 1
    if n in dict_pow:
        return dict_pow[n]
    if n > 0:
        if n % 2 == 0:
            dict_pow[n] = myPow(x, n // 2) * myPow(x, n // 2)
            return dict_pow[n]
        else:
            dict_pow[n] = x * myPow(x, n - 1)
            return dict_pow[n]
    if n < 0:
        return 1 / x * myPow(x, (n + 1))

print(myPow2(2.100, 3))
print(myPow2(2.000, -2))
