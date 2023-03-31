# https://leetcode.com/problems/partition-labels/
def find_partition_labels(s):
    last_found_map = {}
    for i, c in enumerate(s):
        last_found_map[c] = i
    print(last_found_map)
    j = 0
    anchor = 0
    ans = []
    for i, c in enumerate(s):
        j = max(j, last_found_map[c])
        if j == i:
            ans.append(j - anchor + 1)
            anchor = j + 1
    print(ans)


# find_partition_labels("ababcbacadefegdehijhklij")