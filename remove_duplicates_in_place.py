"""
sorted array : [1,1,1,2,2,3,3,3,3,4,4]
output : [1,2,3,4]

Remove the duplicates in-place and O(n).
"""


def remove_duplicates(arr):
    pos = 0
    for i in range(len(arr)-1):
        if arr[i] != arr[i + 1]:
            pos += 1
            arr[pos] = arr[i + 1]

    while len(arr) > pos + 1:
        arr.pop()

    print(arr)


remove_duplicates([1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4])
remove_duplicates([1,2,3,4])
remove_duplicates([-1, -1, 0, 20, 20, 20, 45, 50])
