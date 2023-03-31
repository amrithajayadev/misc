from typing import List


def three_sums(nums: List[int]) -> List[List[int]]:
    triplets = list()
    for i_idx, i in enumerate(nums):
        triplet = list()
        triplet.append(i)
        for j in nums[i_idx + 1:]:
            triplet.append(j)
            sum_i_j = sum(triplet)
            i_index = 1 if i_idx == 0 else i_idx
            j_idx = i_index + nums[i_idx + 1:].index(j)
            if sum_i_j * -1 in nums[j_idx + 1:]:
                triplet.append(sum_i_j * -1)
                triplets.append(triplet)
                print(triplet)
                break
            else:
                triplet.pop()
    return triplets


# triplets = three_sums([-1, 0, 1, 2, -1, -4])


def two_sums(arr, number) -> List:
    couples = []
    for i in range(len(arr)):
        target = number - arr[i]
        if target in arr[i+1:]:
            couples.append([arr[i], target])
    print(couples)
    return couples


def triplet_already_present(triplet, triplets) -> bool:
    for t in triplets:
        l = triplet + t
        res = l[0]
        for i in range(1, len(l)):
            res = res ^ l[i]
        if res == 0:
            return True
    return False


def three_sums_1(nums):
    triplets = []
    for i in range(len(nums)):
        couples = two_sums(nums[i + 1:], nums[i] * -1)
        for couple in couples:
            triplet = []
            triplet.append(nums[i])
            triplet.extend(couple)
            if not triplet_already_present(triplet, triplets):
                triplets.append(triplet)
    return triplets


print(three_sums_1([-1,0,1,2,-1,-4,-2,-3,3,0,4]))