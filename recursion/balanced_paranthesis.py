# n = 3
#
#
# def solve(n, output, stack):
#     if n == 0:
#         if not stack:
#             output = output + '()'
#         else:
#             while stack:
#                 output = output + ')'
#                 stack.pop()
#         print(output)
#     elif n >= 1:
#         solve(n - 1, output + ")", stack)
#         for i in range(2):
#             stack.append('(')
#         solve(n - 1, output + "(", stack)


stack = ['(']


# solve(3, "(", stack)

def solve2(output, open, close):
    if open == 0 and close == 0:
        print(output)
        return
    if open > 0:
        solve2(output + "(", open - 1, close)
    if close > 0 and close > open:
        solve2(output + ")", open, close - 1)


open = 2
close = 3

# solve2("(", open, close)


def generate(o, c, path, ret, n):
    if len(path) == n*2:
        ret.append(path)
        return
    if o < n:
        generate(o + 1, c, path + "(", ret, n)
    if c < n and c < o:
        generate(o, c + 1, path + ")", ret, n)


ret = []
generate(0,0,"", ret, 3)
print(ret)