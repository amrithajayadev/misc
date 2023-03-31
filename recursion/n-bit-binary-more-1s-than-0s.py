n = 5


def generate(ones, zeroes, n, out):
    if n == 0:
        print(out)
    if ones <= n + ones:  # why ??
        generate(ones + 1, zeroes, n - 1, out + '1')
    if zeroes <= ones:
        generate(ones, zeroes + 1, n - 1, out + '0')


generate(0, 0, n - 1, "1")

# def main(n):
#     ones = 0
#     zeroes = 0
#
#     while ones >= zeroes:
#         out = "1"
#         generate(ones - 1, zeroes, out)
#         ones -= 1
#         zeroes += 1
#
#
# main(4)