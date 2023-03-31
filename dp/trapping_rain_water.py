def greatest_element_right(nums):
    output = [nums[-1],]
    for i in range(len(nums) - 2, -1, -1):
        output.append(max(nums[i], output[-1]))

    print(output[::-1])
    return output[::-1]


def greatest_element_left(nums):
    output = []
    for i in range(len(nums)):
        if not output:
            output.append(nums[i])
        else:
            output.append(max(output[i-1], nums[i]))
    print(output)
    return output


# nums = [2, 1, 5, 6, 2, 3, 2, 2]  # [-1, 2, -1, -1, 6, 6,3,2]
# nearest_greatest_element_left(nums)


def rain_water_trapped(heights):
    ngl = greatest_element_left(heights)
    ngr = greatest_element_right(heights)

    water = 0
    for i in range(len(heights)):
        water += min(ngr[i], ngl[i]) - heights[i]

    return water


heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# heights = [4,2,0,3,2,5]
print(rain_water_trapped(heights))