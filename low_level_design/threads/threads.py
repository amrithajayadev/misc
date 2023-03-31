import threading as th


def print_odd(n):
    for i in range(1, n, 2):
        print(i)


def print_even(n):
    for i in range(0, n, 2):
        print(i)


if __name__ == "__main__":
    limit = 30
    even_t = th.Thread(target=print_even, args=(limit,))
    odd_t = th.Thread(target=print_odd, args=(limit,))

    even_t.start()
    odd_t.start()

    even_t.join()
    odd_t.join()
