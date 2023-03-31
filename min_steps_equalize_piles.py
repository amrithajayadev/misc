# https://leetcode.com/discuss/interview-question/364618/

def count_min_steps_equalize(arr):
    arr.sort(reverse=True)  # O(nlogn)
    steps = 0
    n = len(arr)
    i = 0
    while i in range(n-1):  # O(n)
        if arr[i] > arr[i+1]:
            # for k in range(0,i+1):  # O(n)
            #     arr[k] = arr[i+1]
            #     steps += 1
            steps += i+1
        i += 1
    return steps

# piles = [5, 2, 1]
# piles = [1,1,2,2,2,3,3,3,4,4]
# piles = [2,1]
# piles = [10, 10]
# piles = []
# piles = [4,5,5,4,2]
# piles = [4,8,8]
piles = [5,2,1,6]
print(count_min_steps_equalize(piles))