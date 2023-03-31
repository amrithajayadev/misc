# https://leetcode.com/problems/find-the-town-judge/

def find_town_judge1(trust):
    most_trusted = {}
    people = set()
    for item in trust:
        p, t = item
        if t in most_trusted:
            most_trusted[t] += 1
        else:
            most_trusted[t] = 1
        people.add(p)
    max_trust = 0
    tj = None
    for k, v in most_trusted.items():
        if v > max_trust:
            max_trust = v
            tj = k

    if tj in people:
        return -1
    else:
        return tj

def find_town_judge(n, trust):
    count = [0] * (n + 1)
    for i, j in trust:
        count[i] -= 1
        count[j] += 1
    for i in range(1, n + 1):
        if count[i] == n - 1:
            return i
    return -1
# trust = [[1,2]]
# trust = [[1,3],[2,3]]
# trust = [[1, 3], [2, 3], [3, 1]]
trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
print(find_town_judge(4, trust))