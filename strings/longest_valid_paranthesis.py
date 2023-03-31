def find_longest_valid_paranthesis(s):
    stack = []
    for i, char in enumerate(s):
        if char == "(":
            stack.append(["(", i])
        elif char == ")":
            if stack and stack[-1][0] == "(":
                stack.pop()
            else:
                stack.append([")", i])

    lengths = []
    lengths.append(stack[0][1])
    for i in range(1,len(stack)):
        lengths.append(stack[i][1]-stack[i-1][1]-1)
    lengths.append(len(s)-stack[-1][1]-1)
    print(lengths)
    return max(lengths)


print(find_longest_valid_paranthesis("()(()"))