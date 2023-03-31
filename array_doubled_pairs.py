# https://leetcode.com/problems/array-of-doubled-pairs/
import collections


# nums = [4, -2, 2, -4]
# nums = [1, 3, 3, 6]
# nums = [1, 2, 4, 16, 8, 4]
# nums = [2, 4, 0, 0, 8, 1]

# nums = [-8, -4, -2, -1, 0, 0, 1, 2, 4, 8]


def double_arr(nums):
    nums.sort(reverse=True)
    doubled_nums = [2 * i for i in nums]
    pairs = []
    for idx, n in enumerate(doubled_nums):
        if n in nums:
            idx1 = nums.index(n)
            pairs.append(n)
            nums.pop(idx1)
            try:
                idx2 = nums.index(n // 2)
                pairs.append(n // 2)
                nums.pop(idx2)
            except Exception:
                return False

    if len(pairs) == len(doubled_nums):
        return True
    else:
        return False


# if double_arr(nums):
#     print("true")
# else:
#     print("false")

# nums1 = [-8, -4, -2, -1, 0, 0, 1, 2, 4, 8]


def can_reorder(nums1):
    count = collections.Counter(nums1)
    for x in sorted(nums1, key=abs):
        if count[x] == 0:
            continue
        if count[2 * x] == 0:
            return False
        count[x] -= 1
        count[2 * x] -= 1
    print(count)

    return True


# can_reorder(nums1)


def find_original_arr(changed):
    if len(changed) % 2 != 0:
        return []
    count = collections.Counter(changed)
    orig = []
    for x in sorted(changed, key=abs, reverse=True):
        if count[x] == 0:
            continue
        if count.get(2 * x) == 0 or count.get(2 * x) is None:
            continue
        if x != 0:
            count[x * 2] -= 1
            count[x] -= 1
            # print(count)
            orig.append(x)
        else:
            if count[0] % 2 == 0 and count[0] > 0:
                orig.append(0)
                count[0] -= 2

    return orig if len(orig) == len(changed) // 2 else []


#
# print(find_original_arr([-8, -4, -2, -1, 0, 0, 1, 2, 4, 8]))
# print(find_original_arr([1, 3, 4, 8]))
# print(find_original_arr([2, 1, 2, 4, 2, 4]))
# print(find_original_arr([6,3,0,1]))

def find_orig_arr_with_k(nums):
    even = []
    odd = []
    orig = []
    even_c = 0
    odd_c = 0
    nums.sort()
    # n = len(nums)
    for n in nums:
        if n % 2 == 0:
            even_c += 1
        else:
            odd_c += 1
    if even_c == 0 or odd_c == 0 or even_c % odd_c !=0:
        l = len(nums) // 2
        for i in range(l):
            orig.append((nums[i] + nums[i + l]) // 2)
        print(orig)
    else:
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                if not even or even[-1] == nums[i]:
                    even.append(nums[i])
                else:
                    orig.append((even[-1] + nums[i]) // 2)
                    even.pop()
            else:
                if not odd or odd[-1] == nums[i]:
                    odd.append(nums[i])
                else:
                    orig.append((odd[-1] + nums[i]) // 2)
                    odd.pop()
        print(orig)


find_orig_arr_with_k(nums=[11, 6, 3, 4, 8, 7, 8, 7, 9, 8, 9, 10, 10, 2, 1, 9])
find_orig_arr_with_k(nums=[2, 10, 6, 4, 8, 12])
find_orig_arr_with_k([1, 1, 3, 3])
find_orig_arr_with_k([4, 6, 8, 8, 4, 4, 2, 3, 6, 6, 10, 4, 9, 10, 5, 11])
find_orig_arr_with_k([1,50,99,101,150,199])