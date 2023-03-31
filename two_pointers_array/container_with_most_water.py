def max_water(heights):
    start = 0
    end = len(heights)-1
    max_water = 0
    while start < end:
        h = min(heights[start], heights[end])
        vol = h*(end-start)
        max_water = max(vol, max_water)
        if heights[start] < heights[end]:
            start += 1
        else:
            end -= 1
    return max_water


print(max_water([1,8,6,2,5,4,8,3,7]))