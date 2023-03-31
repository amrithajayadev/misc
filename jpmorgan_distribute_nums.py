def distribute_nums(nums, n):
    sol = []
    i = 0
    while i < len(nums):
        for j in range(n):
            if i < n:
                sol.append([nums[i]])
            elif i < len(nums):
                sol[j].append(nums[i])
            else:
                break
            i += 1
    print(sol)

distribute_nums([1,2,3,4,5,6,7,8,9,10, 11], 3)