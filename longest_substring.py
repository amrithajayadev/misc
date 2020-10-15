# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 19:57:12 2019

@author: jayada1
"""


# def twoSum(self, nums: List[int], target: int) -> List[int]:
def twoSum(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        if nums[left] + nums[right] == target:
            return [left, right]
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            left += 1
    return []


def twosums(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


nums = [3, 2, 4]
target = 8
twosums(nums, target)

twoSum(nums, target)


def mutateTheArray(n, a):
    b = list()
    b.append(a[0] + a[1])
    for i in range(1, n - 1):
        val = a[i - 1] + a[i] + a[i + 1]
        b.append(val)
    b.append(a[-1] + a[-2])
    print(b)


a = [4, 0, 1, -2, 3]
mutateTheArray(5, a)


def alternatingSort(a):
    left = 0
    right = len(a) - 1
    c = 0
    b = list()
    while left <= right:
        if c % 2 == 0:
            b.append(a[left])
            left += 1
        else:
            b.append(a[right])
            right -= 1
        c += 1
    c = a[:]
    c.sort()
    print(b)
    print(c)
    if b == c:
        return True
    else:
        return False


a1 = [1, 3, 5, 6, 4, 2]
a = [-92, -23, 0, 45, 89, 96, 99, 95, 89, 41, -17, -48]
alternatingSort(a)

d = dict()


def insert(q):
    x = q[0]
    y = q[1]
    d[x] = y


def addToValue(q):
    for k, v in d.items():
        d[k] = v + q[0]


def addToKey(q):
    e = dict()
    global d
    for k in d:
        e[k + q[0]] = d.get(k)
    d = e.copy()


def get(q):
    print(d)
    return d.get(q[0])


def hashMap(queryType, query):
    for qt, q in zip(queryType, query):
        if qt == 'insert':
            insert(q)
        elif qt == 'addToValue':
            addToValue(q)
        elif qt == 'addToKey':
            d = addToKey(q)
            print(d)
        elif qt == 'get':
            print(get(q))


queryType = ["insert",
             "insert",
             "addToValue",
             "addToKey",
             "get"]
query = [[1, 2],
         [2, 3],
         [2],
         [1],
         [3]]

hashMap(queryType, query)


def lengthOfLongestSubstring(s: str) -> int:
    unique = list()
    max_len = 0
    for character in s:
        if character not in unique:
            unique.append(character)
        else:
            unique = []
            unique.append(character)

        if max_len < len(unique):
            max_len = len(unique)

    return max_len


lengthOfLongestSubstring("pwwkewb")


def lengthOfLongestSubstring(s: str) -> int:
    unique = list()
    max_len = 0
    for i in range(len(s)):
        unique.append(s[i])
        for j in range(i + 1, len(s)):
            if s[j] not in unique:
                unique.append(s[j])
            else:
                unique = []
                break
            if max_len < len(unique):
                max_len = len(unique)
    return max_len


lengthOfLongestSubstring("bbbb")
