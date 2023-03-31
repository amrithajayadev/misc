# https://leetcode.com/problems/minimum-time-visiting-all-points/

points = [[1, 1], [3, 4], [-1, 0]]
mins = 0
for idx, point in enumerate(points):
    x, y = point
    if idx < len(points)-1:
        x1, y1 = points[idx + 1]
    else:
        x1, y1 = None, None
    x_mins = 0
    y_mins = 0
    while x != x1 and x1 is not None:
        if x < x1:
            x += 1
        elif x > x1:
            x -= 1
        else:
            continue
        x_mins +=1
    while y != y1 and y1 is not None:
        if y < y1:
            y += 1
        elif y > y1:
            y -= 1
        else:
            continue
        y_mins += 1
    mins += max(x_mins,y_mins)
print(mins)
