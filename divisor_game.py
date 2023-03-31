n = 10


def can_a_win(n):
    while n > 1:
        for i in range(2, (n // 2) + 1):
            if n % i == 0:
                n -= i