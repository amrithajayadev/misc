from typing import List


def evalRPN(tokens: List[str]) -> int:
    """
    Convert the tokens to numbers
    Use a stack to store the numbers
    When an operator is encountered, check if there are at least
    2 items on the stack.
    Pop the numbers
    Apply the arithmetic op on the nums
    Add the result back to the stack
    """
    ops = ["+", "-", "*", "/"]
    stack = []
    for t in tokens:
        if t.isnumeric() or (t[0] == "-" and t[1:].isnumeric()):
            stack.append(int(t))
        elif t in ops:
            y = stack.pop()
            x = stack.pop()
            if t == "+":
                res = x + y
            elif t == "*":
                res = x * y
            elif t == "-":
                res = x - y
            elif t == "/":
                if x < 0:
                    res = abs(x)//y
                    res *= -1
                elif y < 0:
                    res = x// abs(y)
                    res *= -1
                else:
                    res = x // y
            print(f"x={x}, y={y}, op={t}, res={res}")
            stack.append(res)
            print(stack)
    return stack[-1]


tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
evalRPN(tokens)
