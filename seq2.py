from collections import deque

def missingDigits(config, x, y):
    # Write your code here
    """
    1. Convert the config to array of integers
    2. cur = 0
    3. Use a decision tree bfs to find a number that satisfies the config
    """
    def reachable_digits(x, y):
        visited = set()
        q = deque([x, y])
        while q:
            d = q.popleft()
            if d in visited:
                continue
            visited.add(d)
            q.append((d+x)%10)
            q.append((d + y) % 10)
        return visited


    n = len(config)
    s = list(map(int, config))
    reach = reachable_digits(x, y)

    for digit in s:
        if digit not in reach:
            return None

    q = deque()
    visited = set()

    parent = {}
    digit_added = {}

    for a in [x, y]:
        digit = a % 10
        matched = 1 if digit == s[0] else 0
        state = (digit, matched)
        q.append(state)
        visited.add(state)

        parent[state] = None
        digit_added[state] = digit

    while q:
        digit, matched = q.popleft()
        if matched == n:
            result = []
            state = (digit, matched)

            while state:
                result.append(str(digit_added[state]))
                state = parent[state]
            return "".join(result[::-1])

        for a in [x, y]:
            next_digit = (digit + a) % 10
            next_matched = matched

            if matched < n and next_digit == s[matched]:
                next_matched += 1

            state = (next_digit, next_matched)
            if state not in visited:
                visited.add(state)
                parent[state] = (digit, matched)
                digit_added[state] = next_digit
                q.append(state)

    return "-1"

print(missingDigits("27",2,3))
print(missingDigits("324", 2,3))