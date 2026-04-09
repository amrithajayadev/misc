from collections import Counter
from typing import List


def threeSumMulti(arr: List[int], target: int) -> int:
    arr.sort()
    freq_map = Counter(arr)
    st = list(set(arr))
    res = 0
    triplets = set()
    # for distinct integers
    print(f"st={st}")
    for i in range(len(st) - 2):
        for j in range(i + 1, len(st) - 1):
            curr_triplet = [st[i], st[j], target - (st[i] + st[j])]
            curr_triplet.sort()
            if target - (st[i] + st[j]) in freq_map and tuple(curr_triplet) not in triplets:
                print(f"arr[i],arr[j],arr[k]:{st[i]},{st[j]}, {target - (st[i] + st[j])}")
                res += freq_map[target - (st[i] + st[j])]
                print(f"res={res}, freq_map[{target - (st[i] + st[j])}]={freq_map[target - (st[i] + st[j])]}")
                triplets.add(tuple(curr_triplet))
            res += freq_map[st[j]]
        res += freq_map[st[i]]
    print(f"res after distinct:{res}")

    # repeating integers can be
    for k, v in freq_map.items():
        if v >= 3 and k * 3 == target:
            print(f"Processing k={k} with v=3")
            res += 3
        elif v >= 2 and k * 2 < target and target - (k * 2) in freq_map:
            curr_triplet = [k, k, target - (k * 2)]
            curr_triplet.sort()
            if tuple(curr_triplet) not in triplets:
                print(f"Processing k={k} with v=2")
                res += freq_map[target - (k * 2)]
                triplets.add(tuple(curr_triplet))
    print(f"res after repeating:{res}")
    return res


# arr = [1,1,2,2,3,3,4,4,5,5]
# arr = [2, 1, 3]
# target = 6

arr=[1,1,2,2,2,2]
target =5
print(threeSumMulti(arr, target))
