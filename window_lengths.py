def find_window_length(marker):
    final_intervals = []
    start = 0
    end = 0
    while end < len(marker):
        if marker[start] == 0:
            start += 1
            end += 1
            continue
        if marker[end] == 1:
            end += 1
        elif marker[end] == 0:
            final_intervals.append([start, end])
            start = end
    print(final_intervals)


marker = [0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0]


# find_window_length(marker)


def merge(intervals):
    marker = [0] * 10
    final_intervals = []
    single_intervals = []
    for interval in intervals:
        for i in range(interval[0], interval[1]):
            marker[i] = 1
        if interval[0] == interval[1]:
            single_intervals.append(interval)
    for interval in single_intervals:
        if marker[interval[0]] != 1:
            final_intervals.append(interval)
    print(marker)
    start = 0
    end = 0
    while end < len(marker):
        if marker[start] == 0:
            start += 1
            end += 1
            continue
        if marker[end] == 1:
            end += 1
        elif marker[end] == 0:
            final_intervals.append([start, end])
            start = end
    print(final_intervals)


# merge([[1,4],[5,6]])
# merge([[1,3],[2,6],[8,10],[15,18]])
# merge([[1, 4], [0, 0]])
# merge([[2, 3], [2, 2], [3, 3], [1, 3], [5, 7], [2, 2], [4, 6]])


def merge_intervals(intervals):
    out = []
    out.append(intervals[0])
    for start, end in intervals:
        if out[-1][0] <= start < out[-1][1] < end:
            out[-1][1] = end
        elif out[-1][1] < start:
            out.append([start, end])
    print(out)


# merge_intervals([[2, 3], [2, 2], [3, 3], [1, 3], [5, 7], [2, 2], [4, 6]])


def insert_interval(intervals, newInterval):
    out = []
    for i, interval in enumerate(intervals):
        if interval[0] <= newInterval[0] <= interval[1] <= newInterval[1]:
            interval[1] = newInterval[1]
            out.append(interval)
        elif newInterval[0] > interval[0]:
            out.append(interval)
        elif out[-1][0] <= interval[0] <= out[-1][1] < interval[1]:
            out[-1][1] = interval[1]
        elif out[-1][1] < interval[0]:
            out.append(interval)
    print(out)

#
# intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
# newInterval = [4, 8] o/p [[1, 2], [3, 10], [12, 16]]

intervals = [[1,3],[6,9]]
newInterval = [2,5]
insert_interval(intervals, newInterval)