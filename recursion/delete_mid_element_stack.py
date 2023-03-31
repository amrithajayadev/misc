s = [1, 3, 4, 2, 6]
mid = len(s) // 2+ 1


def delete_mid_element(arr, mid):
    if mid == 1:
        arr.pop()
        return arr
    else:
        temp = arr.pop()
        delete_mid_element(arr, mid - 1)
        arr.append(temp)


delete_mid_element(s, mid)
print(s)
