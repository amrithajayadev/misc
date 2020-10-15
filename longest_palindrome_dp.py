def reverse_string(s):
    l = 0
    r = len(s) - 1
    s1 = list(s)
    while l < r:
        s1[l], s1[r] = s1[r], s1[l]
        l += 1
        r -= 1

    rs = ''.join(s1)
    return rs

s = "amritha"
rev = reverse_string(s)
print(s)
print(rev)


def removeDuplicates(nums) -> int:
    n = len(nums)-1
    c = 0
    i = 0
    while i < n:
        if nums[i] < nums[i + 1]:
            if c >= 1:
                nums.pop(i-1)
                n -= 1
            c = 0
        else:
            c += 1
            if c > 1:
                nums.pop(i)
                n -= 1
                c -= 1
        i += 1
    return nums