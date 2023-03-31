# https://leetcode.com/problems/top-k-frequent-words/
import heapq
from collections import Counter
from typing import List


class Node:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq

    def __eq__(self, other):
        return self.word == other.word and self.freq == other.freq


# O(n log k) solution
def top_k_words(words, k):
    freq_map = Counter(words)
    print(freq_map)
    res = []
    heapq.heapify(res)

    for word, f in freq_map.items():
        heapq.heappush(res, Node(word, f))
        if len(res) > k:
            heapq.heappop(res)

    out = []
    for _ in range(k):
        w = heapq.heappop(res)
        out.append(w.word)
    print(out)


def topKFrequent(words: List[str], k: int) -> List[str]:  # O(n log n) solution
    dict = {}
    for x in words:
        if x in dict:
            dict[x] += 1
        else:
            dict[x] = 1
    res = sorted(dict, key=lambda x: (-dict[x], x))
    return res[:k]


words = ["i", "love", "leetcode", "i", "love", "coding", "k", "k"]
k = 2

# words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
# k = 4

top_k_words(words, k)


def top_k_nums(nums, k):  ## also O(nlogn) because creating heap from full nums.
    k_large = 0
    heapq.heapify(nums)
    while k > 0:
        k_large = heapq.heappop(nums)
        k -= 1
    return k_large

# print(top_k_nums([1, 2, 3, 4, 5, 6], 4))


def bin_sort(nums):
    i = 0
    j = len(nums) - 1
    while i <= j:
        if nums[i] < nums[j]:
            i += 1
        elif nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        else:
            if nums[i] == 0:
                i += 1
            else:
                j -= 1
    print(nums)

#
# bin_sort([1, 0, 1, 1, 0])
# bin_sort([1, 0, 1, 1, 1])
# bin_sort([0, 0, 0, 0, 0])
# bin_sort([1, 1, 1, 1, 1])
# bin_sort([1, 1, 1, 0, 0, 0])
# bin_sort([1, 0, 1, 0, 1, 0])
# bin_sort([0, 0, 1, 0, 1, 1])
