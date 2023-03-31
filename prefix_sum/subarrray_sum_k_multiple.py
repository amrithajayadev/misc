def subarray_sum_k_multiple(nums, k) -> bool:
    prefix_sum = { 0: -1}
    curr_sum = 0
    for i, n in enumerate(nums):
        curr_sum += n
        mod = curr_sum % k
        if mod in prefix_sum:
            if i-prefix_sum[mod] > 1:
                return True
        else:
            prefix_sum[mod] = i
    return False



# nums = [23,2,4,6,7]
# k = 6
#
# nums = [24,3,4,6,7]
# k = 6

# nums = [23,2,4,6,6]
# k = 7

nums = [5,0,0,0]
k = 3
if subarray_sum_k_multiple(nums, k):
    print("True")
else:
    print("False")