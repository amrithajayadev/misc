# original = [5, 2, 4, 3, 1, 6] #works
# original = [1,2,3,4] #works
# original = [3, 6, 4, 2, 1] #works
original = [4,3,2,1]
temp_stack = []
sorted_stack = []

while original:
    if not sorted_stack:
        sorted_stack.append(original.pop())

    while sorted_stack:
        if original[-1] > sorted_stack[-1]:
            temp_stack.append(sorted_stack.pop())
        else:
            break
    sorted_stack.append(original.pop())
    while temp_stack:
        sorted_stack.append(temp_stack.pop())

print(sorted_stack)
print(original)
