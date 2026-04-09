from collections import deque
def missingDigits(config, x, y):
    # Write your code here
    """
    1. Convert the config to array of integers
    2. cur = 0
    3. Use a decision tree bfs to find a number that satisfies the config
    """

    n = len(config)
    s = list(map(int, config))

    q = deque()
    visited = set()

    for a in [x, y]:
        digit = a % 10
        matched = 1 if digit == s[0] else 0
        state = (digit, matched, str(digit))
        q.append(state)
        visited.add((digit, matched))

    while q:
        digit, matched, seq = q.popleft()
        if matched == n:
            return seq
        for a in [x, y]:
            next_digit = (digit + a) % 10
            next_matched = matched

            if matched < n and next_digit == s[matched]:
                next_matched += 1

            state_key = (next_digit, next_matched)
            if state_key not in visited:
                visited.add(state_key)
                q.append((next_digit, next_matched, seq + str(next_digit)))

    return -1

print(missingDigits("521",5,5))