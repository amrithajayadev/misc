# https://leetcode.com/problems/remove-k-digits/

def remove_k_digits(num, k):
    stack = []
    len_out = len(num) - k
    if len_out <= 0:
        return "0"
    last_pos = {}
    for i, n in enumerate(num):
        last_pos[n] = i

    for i in range(len(num)):
        while stack and k and (stack[-1] > num[i]):
            stack.pop()
            k -= 1
        stack.append(num[i])
    if k:
        stack = stack[:-k]
    print(stack)
    print(int(''.join(stack)))
    return int(''.join(stack))

remove_k_digits("1992291", 3)
remove_k_digits("1222221", 3)
remove_k_digits("10200", 1)
remove_k_digits("1432219", 3)
remove_k_digits("112", 1)