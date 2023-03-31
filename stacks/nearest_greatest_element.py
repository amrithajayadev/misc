# arr = [2, 3, 5, 1, 10, 4, 6]  # works
arr = [2, 1, 5, 6, 2, 3, 2, 2]
arr2 = [4, 5, 2, 25]  # works
arr3 = [100, 2, 3, 4]  # works


# arr = [1, 0]  # works

def nearest_greatest_to_right(arr):
    stack = []
    output = []
    n = len(arr)
    for i in range(n - 1, -1, -1):
        if not stack:
            output.append(-1)
        else:
            if arr[i] <= stack[-1]:
                output.append(stack[-1])
            else:
                while stack and arr[i] >= stack[-1]:
                    stack.pop()
                if stack:
                    output.append(stack[-1])
                else:
                    output.append(-1)
        stack.append(arr[i])
    print("nearest_greatest_to_right")
    return output[::-1]


# Check the elements to the right of the number to know if any element>num.
# Since we check the right, start with the rightmost element. Rightmost element always returns -1
# The output will be stored in output array, push -1 to output array.

# If the element in arr is greater than the element on top of stack, pop elements until there is a bigger element or until the stack becomes empty.
### If the stack is empty, it means that no element is greater than the arr element. So push -1 to output.
### If the stack is not empty, push the top of the stack to output.
# If the next element in arr is smaller than the element on top of stack, then push top_of_stack element to output.
# Once an element is processed, push it into the stack.

# Repeat the steps above until all the elements in the arr are covered.

def nearest_greatest_to_left(arr):
    stack = []
    output = []
    n = len(arr)
    for i in range(0, n):
        if not stack:
            output.append(-1)
        else:
            if stack[-1] >= arr[i]:
                output.append(stack[-1])
            else:
                while stack and stack[-1] < arr[i]:
                    stack.pop()
                if stack:
                    output.append(stack[-1])
                else:
                    output.append(-1)
        stack.append(arr[i])
    print("nearest_greatest_to_left")
    return output


# arr = [2, 3, 5, 1, 10, 4, 6]
def nearest_smallest_to_right(arr):
    stack = []
    output = []
    n = len(arr)
    for i in range(n - 1, -1, -1):
        if not stack:
            output.append(-1)
        else:
            if stack and arr[i] > stack[-1]:
                output.append(stack[-1])
            else:
                while stack and stack[-1] >= arr[i]:
                    stack.pop()
                if stack:
                    output.append(stack[-1])
                else:
                    output.append(-1)
        stack.append(arr[i])
    return output[::-1]


# arr = [2, 3, 5, 1, 10, 4, 6]
def nearest_smallest_element_to_left(arr):
    stack = []
    output = []
    n = len(arr)
    for i in range(0, n):
        if not stack:
            output.append(-1)
        else:
            if stack[-1] < arr[i]:
                output.append(stack[-1])
            else:
                while stack and stack[-1] >= arr[i]:
                    stack.pop()
                if stack:
                    output.append(stack[-1])
                else:
                    output.append(-1)
        stack.append(arr[i])
    return output

print(nearest_greatest_to_left(arr))
# nearest_smallest_to_right(arr)
# nearest_smallest_element_to_left(arr)
print(nearest_greatest_to_right(arr))
# [3, 5, 10, 10, -1, 6, -1]