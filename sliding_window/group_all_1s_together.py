# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/

def group_all_ones(arr):
    window_size = sum(x == 1 for x in arr)
    i = 0
    j = 0
    swaps = len(arr) + 1
    arr += arr
    while j < len(arr)-1+window_size-1:
        if j -i- 1< window_size:
            j +=1
        else:
            num_zeroes = sum(x == 0 for x in arr[i:j])
            swaps = min(swaps, num_zeroes)
            # print(i, j, swaps)
            i += 1
            j += 1
    return swaps

print(group_all_ones([0,1,0,1,1,0,0]))
print(group_all_ones([0,1,1,1,0,0,1,1,0]))
print(group_all_ones([1,1,0,0,1]))