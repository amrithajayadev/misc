# https://leetcode.com/problems/last-stone-weight/

stones = [2, 7, 4, 1, 8, 1]

# bruteforce
def break_stone(stones):
    s = sorted(stones)
    while s:
        if len(s) <= 1:
            break
        s.sort()
        if s[-1] > s[-2]:
            max_ele = s.pop()
            s[-1] = max_ele - s[-1]
        else:
            s.pop()
            if s:
                s.pop()
        # print(s)
    print(s)


break_stone(stones)
# feels like a heap problem because we need largest and second largest element in each iteration