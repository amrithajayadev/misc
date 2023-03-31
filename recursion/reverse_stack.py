s = [1, 2, 3, 4, 5]


def reverse_with_extraspace(s, n, temp):
    if n == 0:
        return
    else:
        temp.append(s.pop())
        reverse_with_extraspace(s, n - 1, temp)


temp = []
reverse_with_extraspace(s, 5, temp)
print(temp)
