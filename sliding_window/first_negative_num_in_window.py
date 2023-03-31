arr = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3
n = len(arr)


def first_neg_window_brute(arr, k):
    i = 0
    j = i + k - 1
    first_neg = []

    while j < len(arr):
        k = i
        while k < j:
            if arr[k] > 0:
                k += 1
            else:
                first_neg.append(arr[k])
                break
        i += 1
        j += 1

    print(first_neg)


def first_neg_num_in_window(arr, k, n):
    first_neg = []
    negs = []
    i = 0
    j = 0
    while j < n:
        if arr[j] < 0:
            negs.append(arr[j])
        if j - i + 1 < k:
            j += 1
        elif j - i + 1 == k:
            if negs:
                first_neg.append(negs[0])
                if arr[i] == negs[0]:
                    negs.pop(0)
            else:
                first_neg.append(0)
            i += 1
            j += 1
    print(first_neg)


first_neg_num_in_window(arr, k, n)
