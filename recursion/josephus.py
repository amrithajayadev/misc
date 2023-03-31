def solve(arr, start, n, k):
    if n == 1:
        return arr[0]
    start = (start + k) % n
    if arr:
        arr.pop(start)
    print(arr)
    return solve(arr, start, n - 1, k)


# n = 7
# k = 3
#
n = 5
k = 2


def main(n, k):
    arr = [i for i in range(1, n + 1)]
    print(solve(arr, 0, n, k))


# main(n, k)


def josephus2(arr, n, k, curr):
    if n == 1:
        print(arr[0])
        return
    elif n > 1:
        curr = (curr + k - 1) % n
        arr.pop(curr)
        josephus2(arr, n - 1, k, curr)


def josephus_iter(n, k, curr):
    arr = [i for i in range(1, n + 1)]
    while n > 1:
        curr = (curr + k - 1) % n
        arr.pop(curr)
        n -= 1
    return arr[0]

def main2(n, k):
    arr = [i for i in range(1, n + 1)]
    josephus2(arr, n, k, 0)
    print(josephus_iter(n, k, 0))

main2(40, 7)
