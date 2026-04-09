"""
Given a list of meetings, represented as tuples with a start and an end time, determine the minimum number of rooms required to schedule all the meetings.
Input: meetings = [[5, 10], [2, 3]] Output: 1
Input: meetings = [[1, 3], [5, 7], [4, 6], [7, 9], [9, 10]] Output: 2
"""


# Objective is to find if there are any overlapping times.
# Sort the meetings in chronological order
# Iterate the array to check for overlaps by comparing previous element's end time with next elements start time.
# Increment the count if there is an overlap.

# Sort
# Store the start and end times in a list
# iterate through start and end times array. Base case, increment count to 1
# Increment start pointer and compare with end pointer.
#   if it is lesser, then increment room count.
#   If it is higher or equal, then move end pointer.

# Test case 3
# Input : [[1,3], [2,4], [3,7], [4,5]] Output = 2

# Test case 4
# Input : [[1,3], [2,4], [5,7], [6,8]] Output = 2

def sort(meetings):
    for i in range(len(meetings)):
        for j in range(i + 1, len(meetings)):
            if meetings[i][0] > meetings[j][0]:
                meetings[i], meetings[j] = meetings[j], meetings[i]


def meeting_room_count(meetings):
    sort(meetings)
    print(meetings)
    count = 0
    start_times = []
    end_times = []

    for st, end in meetings:
        start_times.append(st)
        end_times.append(end)

    i = 0
    j = 0
    while i < len(start_times) and j < len(end_times):
        if start_times[i] < end_times[j]:
            count += 1
        else:
            j += 1
        i += 1
    return count

print(meeting_room_count([[5, 10], [2, 3]]))
print(meeting_room_count([[1, 3], [5, 7], [4, 6], [7, 9], [9, 10]]))
print(meeting_room_count([[1,3], [2,4], [3,7], [4,5]]))
print(meeting_room_count([[1,3], [2,4], [5,7], [6,8]]))