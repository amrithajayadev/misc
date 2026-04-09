"""
You are given a list of reservation intervals, where each interval is a pair of dates $[start\_date, end\_date]$.
Given a specific month and year, find the maximum number of overlapping intervals (peak occupancy)
that occur within that month.

1.Sort the intervals by date
2.Iterate through the list
3. If curr_start_date < previous_end_date -> overlapp present : increment the count
4. if curr_start_date
"""


def find_overlaps(arr):
    events = []
    for in1, out in arr:
        events.append((in1, 1))
        events.append((out, -1))

    events.sort()
    max_len = 0
    curr_len = 0
    for e, v in events:
        curr_len += v
        max_len = max(max_len, curr_len)
    return max_len


# arr = [[1, 2], [5, 6], [3, 6], [4, 5]]
arr = [[0,1], [1,3], [0,4], [2,3]]
arr = [[0,1], [1,3], [0,4], [2,3],[6,10],[10,10]]
print(find_overlaps(arr))
