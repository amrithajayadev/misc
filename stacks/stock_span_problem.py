arr = [100, 80, 60, 70, 60, 75, 85]


def stock_span(arr):
    stack = []
    output = []
    n = len(arr)
    for i in range(0, n):
        if not stack:
            output.append(0)
        else:
            if stack[-1] > arr[i]:
                output.append(0)
            else:
                count = 0
                temp = []
                while stack and stack[-1] < arr[i]:
                    temp.append(stack.pop())
                    count = count + 1
                stack.extend(temp)
                output.append(count)
        stack.append(arr[i])
    print(output)


stock_span(arr)


# store the index of the greatest nearest left element in stack.
# if arr[tps_index] > arr[i], then nothing is smaller than the current number
# if arr[tps_index] < arr[i], then keep popping until a bigger number is encountered.
# Then,current_index to tps_index is values smaller than current value. So, distance between these index => i - tps_idx.
# #### Consecutive smaller element-------
def stock_span_solution(arr):
    stack = []
    output = []
    n = len(arr)
    for i in range(n):
        if not stack:
            output.append(1)
        else:
            if arr[stack[-1]] > arr[i]:
                output.append(i-stack[-1])
            else:
                while stack and arr[stack[-1]] <= arr[i]:
                    stack.pop()
                output.append(i - stack[-1])
        stack.append(i)
    print(output)


stock_span_solution(arr)
