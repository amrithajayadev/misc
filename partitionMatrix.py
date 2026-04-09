from typing import List


def canPartitionGrid(grid: List[List[int]]) -> bool:
    row_sums = [sum(grid[i]) for i in range(len(grid))]
    col_sums = [0] * len(grid[0])
    for r in grid:
        for i in range(len(col_sums)):
            col_sums[i] += r[i]

    # check if we can partition
    def partition_arr(arr):
        n = len(arr)
        print(f"arr={arr}")
        pref = [0] * len(arr)
        pref[0] = arr[0]
        suff = [0] * len(arr)
        suff[-1] = arr[-1]
        for i in range(1, n):
            pref[i] = arr[i] + pref[i - 1]
        print(f"pref={pref}")
        for i in range(n - 2, -1, -1):
            suff[i] = arr[i] + suff[i + 1]
        print(f"suff={suff}")
        for i in range(n - 1):
            if pref[i] == suff[i + 1]:
                return True
        return False
    print(f"Partition rows:{partition_arr(row_sums)}")
    print("------------------")
    print(f"Partition cols:{partition_arr(col_sums)}")
    return partition_arr(row_sums) or partition_arr(col_sums)

print(canPartitionGrid([[1],[1],[2]]))