def feasible(capacity, D, weights):
    total = 0
    days = 0
    for w in weights:
        total += w
        if total > capacity:
            days += 1
            if days > D:
                return False
    return True


def _binary_search(weights, D):
    start = max(weights)
    end = sum(weights)

    while start < end:
        mid = (start + end) // 2
        if feasible(mid, D, weights):
            end = mid
        else:
            start = mid + 1
    return start

# print(_binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))


def shipWithinDays(weights, days: int) -> int:
    start = max(weights)
    end = sum(weights)

    def is_feasible(container_cap):
        d = 1
        wt = 0
        for w in weights:
            wt += w
            if wt > container_cap:
                wt = w
                d += 1
                if d > days:
                    return False
        return True

    while start < end:
        mid = (start + end) // 2
        if is_feasible(mid):
            end = mid
        else:
            start = mid + 1
    return start

print(shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))


def shipWithinDays(weights, days: int) -> int:
    start = max(weights)
    end = sum(weights)

    def feasible(capacity):
        tot = 0
        d = 1
        for w in weights:
            tot += w
            if tot > capacity:
                tot = w
                d += 1
                if d > days:
                    return False
        return True

    while start < end:
        mid = (start + end) // 2
        if feasible(mid):
            end = mid
        else:
            start = mid + 1

    return start

print(shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
