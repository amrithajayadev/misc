# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
s = "abbaca"


# Output: "ca"
def remove_dupes1(s):
    stack = []
    stack = [['#', 0]]
    for elem in s:
        if stack[-1][1] > 1:
            stack.pop()
        if elem == stack[-1][0]:
            stack[-1][1] += 1
        else:
            stack.append([elem, 1])
    return ''.join(i * j for i, j in stack[1:])


# print(remove_dupes1("aaaaaaaaaaaaaa")) # doesn't work

def remove_dupes_soln(s):
    stack = ['#']
    for elem in s:
        if stack and stack[-1] == elem:
            stack.pop()
        else:
            stack.append(elem)
    return ''.join(stack[1:])

print(remove_dupes_soln("aaaaaaaaaaaaaaaaaa"))