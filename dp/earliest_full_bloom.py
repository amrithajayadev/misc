# https://leetcode.com/problems/earliest-possible-day-of-full-bloom/


def find_earliest_bloom(plantTime, growTime):
    p_g = [(p, g) for p, g in zip(plantTime, growTime)]
    p_g.sort(key=lambda x: x[1], reverse=True)
    curr = 0
    res = 0
    for p, g in p_g:
        curr += p
        res = max(res, curr + g)
    print(res)


# plantTime = [1, 4, 3]
# growTime = [2, 3, 1]  # o/p = 9

# plantTime = [1]
# growTime = [1]  # o/p = 2


plantTime = [1,2,3,2]
growTime = [2,1,2,1] # o/p=9

find_earliest_bloom(plantTime, growTime)