def print_r_nto1(n):
    if n == 0:
        return
    print(n, end=" ")
    print_r_nto1(n - 1)


def print_r_1ton(n):
    if n == 0:
        return
    print_r_1ton(n - 1)
    print(n, end=" ")


print_r_nto1(10)
print("\n")
print_r_1ton(10)
