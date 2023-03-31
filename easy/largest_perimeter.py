def largestPerimeter(nums) -> int:
    def is_triangle_valid(nums0, nums1, nums2):
        valid = True
        if nums0 >= nums1 + nums2:
            valid = False
        elif nums1 >= nums2 + nums0:
            valid = False
        elif nums2 >= nums1 + nums0:
            valid = False
        return valid

    nums.sort()
    max_perimeter = 0
    for i in range(0, len(nums)-2):
        if is_triangle_valid(nums[i], nums[i + 1], nums[i + 2]):
            perimeter = nums[i] + nums[i + 1] + nums[i + 2]
            print(perimeter)
            max_perimeter = max(perimeter, max_perimeter)
    return max_perimeter

print(largestPerimeter([3,2,3,4]))