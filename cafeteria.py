def count_diners(N, K, M, S):
    arr = [0]*N
    for i in range(0,N):
        if i+1 in S:
            arr[i] = 1
            if i+K < N-1:
                arr[i+K] = -1
            if i-K >= 0:
                arr[i-K] = -1
# count_diners(10, 1, 2, [2,6])
count_diners(15, 2, 3, [11, 6, 14])