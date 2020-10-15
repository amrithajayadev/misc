# code
t = int(input())


def go_to_dest(a, b, steps):
    x = 0
    y = 0
    count = 0
    # for x in range(a):
    #     count+= 1
    # for y in range(b):
    #     count+= 1

    while x < a:
        x += 1
        if x == a:
            count += 1
            break
        a -= 1
        count += 2

    while y < b:
        y += 1
        if y == b:
            count += 1
            break
        b -= 1
        count += 2

    if count == steps:
        print(1)
    else:
        print(0)


while t > 0:
    a, b, steps = map(int, input().strip().split())
    go_to_dest(a, b, steps)
    t -= 1
