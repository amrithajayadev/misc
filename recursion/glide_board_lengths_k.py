k = 3
l = 0
s = 0
s1 = 2
l1 = 5


def generate(s, l, k, s1, l1, output):
    if k == 0:
        print(output)
        return
    generate(s + 1, l, k - 1, s1, l1, output + s1)
    generate(s, l + 1, k - 1, s1, l1, output + l1)


generate(s, l, k, s1, l1, 0)
