# https://www.hackerrank.com/challenges/frequency-queries/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

def freqQuery(queries):
    freq_map = {}
    res = []
    for q, v in queries:
        if q == 1:
            if freq_map.get(v):
                freq_map[v] += 1
            else:
                freq_map[v] = 1
        elif q == 2:
            if freq_map.get(v):
                freq_map[v] -= 1
                if freq_map[v] == 0:
                    freq_map.pop(v)
        elif q == 3:
            if v in set(freq_map.values()):
                res.append(1)
            else:
                res.append(0)
    # print(freq_map)
    return res

# print(freqQuery([(1,1), (2,2), (3,2), (1,1), (1,1), (2,1), (3,2)]))

print(freqQuery([(1,3), (2,3), (3,2), (1,4), (1,5), (1, 5), (1,4), (3,2), (2,4), (3,2)]))