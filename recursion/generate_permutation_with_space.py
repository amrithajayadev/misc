inp = "ABC"


def generate(inp, out, i):
    if i == len(inp):
        print(out)
        return

    generate(inp, out + inp[i], i + 1)
    generate(inp, out + " " + inp[i], i + 1)


generate("ABC", "A", 1)
