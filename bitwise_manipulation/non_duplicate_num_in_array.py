nums = [-1, 0, 0]
res = nums[0]
for i in range(1, len(nums)):
    res = res ^ nums[i]
print(res)

def check_two_lists_same_elements(l1, l2):
    l3 = l1 + l2
    res = l3[0]
    for i in range(1,len(l3)):
        res = res ^ l3[i]
    if res == 0:
        print("lists contain same elements")
    else:
        print("lists contain different elements")

check_two_lists_same_elements([1,0,-1], [-1, 1, 0])