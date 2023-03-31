# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13
# d e e e d b b c c c b  d  a  a
s = "deeedbbcccbdaa"
k = 3


def remove_dupes(s, i, j, k):
    if j == len(s) - 1:
        print(s)
        return

    while j - i + 1 < k:
        if s[i] == s[j]:
            j += 1
        else:
            i += 1
    s = s[:i] + s[j + 1:]
    remove_dupes(s, i, i + 1, k)


# remove_dupes(s, i, j, k)

def remove_duplicates(s, k):
    while len(s) > k:
        i = 0
        j = 0
        while j - i + 1 <= k and j < len(s):
            if s[i] == s[j]:
                j += 1
            else:
                i += 1
        if j - i == k:
            s = s[:i] + s[j:]
        else:
            break
    print(s)


# remove_duplicates(s, 2)


def remove_duplicate_stack_soln(s,k):
    stack = []
    stack = [['#', 0]]
    for c in s:
        if stack[-1][0] == c:
            stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()
        else:
            stack.append([c, 1])
    return ''.join(c * k for c, k in stack)

# print(remove_duplicate_stack_soln(s,2))

# print(remove_duplicate_stack_soln("deeedbbcccbdaa", 3))  # works
# print(remove_duplicate_stack_soln("abcd", 3)) # works

print(remove_duplicate_stack_soln("yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy", 4))