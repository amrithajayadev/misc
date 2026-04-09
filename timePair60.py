from collections import Counter


def numPairsDivisibleBy60(time):
    """
    :type time: List[int]
    :rtype: int
    """
    res = 0
    time = [x % 60 for x in time]
    print(time)
    for i in range(len(time)):
        hm = Counter(time[i + 1:])
        print(hm)
        if ((60 - time[i])%60) in hm:
            res += hm[(60 - time[i])%60]
            print(res)
    return res

time = [60,60,60]
print(numPairsDivisibleBy60(time))