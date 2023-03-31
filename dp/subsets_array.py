nums = [1, 2, 3]

def get_all_subsets(str1):
    outlist = []

    def subsets(str1, i, out):
        if i == len(str1):
            outlist.append(out)
            return
        subsets(str1, i + 1, out + str1[i])
        subsets(str1, i + 1, out)

    subsets(str1, 0, "")
    print(outlist)


get_all_subsets("abc")

def find_subsets(nums, subset, res):
    res.append(subset)
    for i in range(len(nums)):
        find_subsets(nums[i + 1:], subset + [nums[i]], res)


def subsets(nums):
    res = []
    find_subsets(nums, [], res)
    return res


print(subsets(nums))

def find_permutations_array(nums, perm, res):
    if not nums:
        res.append(perm)
        # return
    for i in range(len(nums)):
        find_permutations_array(nums[:i] + nums[i + 1:], perm + [nums[i]], res)


def permutations(nums):
    res = []
    find_permutations_array(nums, [], res)
    return res


# print(permutations(nums))

def find_permutations_array_with_duplicates(nums, perm, res):
    if not nums:
        res.append(perm)
        return
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        find_permutations_array(nums[:i] + nums[i + 1:], perm + [nums[i]], res)


def permutationsUnique(nums):
    res = []
    nums.sort()
    find_permutations_array_with_duplicates(nums, [], res)
    return res


# print(permutationsUnique([1, 1, 2]))