# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/submissions/


def minRemoveToMakeValid(s: str) -> str:
    stack = []
    s_list = list(s)
    for i, char in enumerate(s):
        if char == '(':
            stack.append(['(', i])
        elif char == ')':
            if stack and stack[-1][0] == '(':
                stack.pop(-1)
            else:
                stack.append([')', i])
    for _, idx in stack[::-1]:
        s_list.pop(idx)

    return "".join(s_list)


# print(minRemoveToMakeValid("))(("))
print(minRemoveToMakeValid("lee(t(c)o)de)"))