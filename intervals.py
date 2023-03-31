# https://leetcode.com/problems/teemo-attacking/

def find_poisoned_secs(timeSeries, duration):
    out = []
    tot = 0
    out.append([timeSeries[0], timeSeries[0] + duration])
    for t in timeSeries:
        if t < out[-1][1]:
            out[-1][1] = t+duration
        else:
            out.append([t, t+duration])

    print(out)
    for start,end in out:
        tot += end-start

    return tot

# timeSeries = [1,4]
# duration = 2

timeSeries = [1,2]
duration = 2
print(find_poisoned_secs(timeSeries, duration))