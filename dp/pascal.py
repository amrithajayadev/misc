# https://leetcode.com/problems/pascals-triangle/

n_rows = 5


def generate_pascal(arr):
    ret = [1]
    for i in range(len(arr) - 1):
        ret.append(arr[i] + arr[i + 1])
    ret.append(1)
    return ret


# print(generate_pascal([1, 4,6, 4, 1]))


def generate_pascals_array(n_rows):
    p_array = [[1]]

    while len(p_array) < n_rows:
        idx = len(p_array) - 1
        p = generate_pascal(p_array[idx])
        p_array.append(p)
    return p_array

# print(generate_pascals_array(5))

def generate_pascal_array_2(n_rows):
    pascals = [[1],[1,1]]
    n = 2
    while n < n_rows:
        pascal = [1,]
        prev_pascal = pascals[n-1]
        for i in range(len(prev_pascal)-1):
            pascal.append(prev_pascal[i]+prev_pascal[i+1])
        pascal.append(1)
        pascals.append(pascal)
        n+=1
    print(pascals)

generate_pascal_array_2(5)