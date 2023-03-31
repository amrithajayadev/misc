import threading as th

even_e = th.Event()
odd_e = th.Event()


def print_even(n):

    for i in range(0, n, 2):
        even_e.wait()
        print(i)
        even_e.clear()
        odd_e.set()


def print_odd(n):
    for i in range(1, n, 2):
        odd_e.wait()
        print(i)
        odd_e.clear()
        even_e.set()


if __name__ == "__main__":
    limit = 30
    even_t = th.Thread(target=print_even, args=(limit,))
    even_t.start()
    odd_t = th.Thread(target=print_odd, args=(limit,))
    odd_t.start()

    even_e.set()

    even_t.join()
    odd_t.join()
