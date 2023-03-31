# arr = ['T', 'T', 'P', 'P', 'T,', 'P']
# k = 2

arr = ['P', 'T', 'T', 'P', 'T']
k = 1


# arr = ['T', 'P', 'P', 'P', 'T', 'T', 'P', 'T', 'P', 'T', 'P', 'P', 'T', 'T', 'P', 'T', 'T', 'P', 'P', 'P', 'P', 'P',
#        'T', 'T', 'P', 'T', 'P', 'T', 'T', 'T', 'P', 'P', 'P', 'P', 'T', 'T', 'P', 'T', 'P', 'T', 'P', 'T', 'T', 'P',
#        'T', 'P', 'T', 'T', 'P', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'P', 'P', 'T', 'P', 'T', 'P', 'T', 'P', 'P', 'T',
#        'T', 'P', 'P', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'P', 'T', 'P', 'P', 'P', 'P', 'T', 'P', 'T',
#        'T']
# k = 4


def find_num_theives_caught(arr, k):
    n = len(arr) - 1
    count = 0
    for i in range(n, -1, -1):
        if arr[i] == 'P':
            for j in range(k, 0, -1):
                if arr[i - j] == 'T':
                    arr[i - j] = 'C'
                    count += 1
                    break
    print(count)
    print(arr)


# find_num_theives_caught(arr, k)


def find_num_theives_caught1(arr, k):
    n = len(arr)
    police = []
    theif = []
    count = 0
    for i in range(n):
        if arr[i] == 'P':
            police.append(i)
        else:
            theif.append(i)
    p = 0
    t = 0

    while p < len(police) and t < len(theif):
        if abs(police[p] - theif[t]) <= k:
            count += 1
            p += 1
            t += 1
        else:
            if police[p] > theif[t]:  # if police is ahead, then look for a closer theif
                t += 1
            else:
                p += 1
    print(count)


find_num_theives_caught1(arr, k)