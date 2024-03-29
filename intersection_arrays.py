# https://leetcode.com/problems/intersection-of-two-arrays-ii/
def intersect(nums1, nums2):
    nums1.sort()
    nums2.sort()

    n1 = len(nums1)
    n2 = len(nums2)
    i = 0
    j = 0
    ret = []
    while i < n1 and j < n2:
        if nums1[i] == nums2[j]:
            ret.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1


intersect(nums1=[1, 2, 2, 1], nums2=[2, 2])