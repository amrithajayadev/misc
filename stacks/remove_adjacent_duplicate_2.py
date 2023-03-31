# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

def remove_duplicates_str(s):
    stack = []

    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    return "".join(stack)


# print(remove_duplicates_str("abbaca"))
# print(remove_duplicates_str("azxxzy"))

# https://leetcode.com/problems/removing-stars-from-a-string/
def remove_stars(s):
    stack = []
    for c in s:
        if c == '*' and stack:
            stack.pop()
        else:
            stack.append(c)
    print("".join(stack))


# remove_stars("leet**cod*e")
# remove_stars("erase*****")

# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
def remove_adjacent_duplicate_with_k(s, k):
    stack = []
    for elem in s:
        if stack and stack[-1][0] == elem:
            stack[-1][1] += 1
        else:
            stack.append([elem, 1])

        if stack[-1][1] == k:
            stack.pop()
    print(stack)
    res = ""
    for elem, count in stack:
        res += elem*count
    print(res)

remove_adjacent_duplicate_with_k("deeedbbcccbdaa", 3)