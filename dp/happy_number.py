sq = [[0] * 10] * 10

for i in range(0, 10):
    for j in range(0, 10):
        val = ((i + 1)**2) + ((j + 1)**2)
        print(f"i={i}, j={j}, i^2+j^2={val}")
        sq[i][j] = val

for k in range(0,10):
    print(sq[k])

assert sq[0][0] == 2
assert sq[0][6] == 50