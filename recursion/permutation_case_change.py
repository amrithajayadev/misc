inp = "a1B2"
diff = ord('a') - ord('A')


def generate(inp, i, out):
    if i == len(inp):
        print(out, end=" ")
        return

    generate(inp, i + 1, out + inp[i])
    if ord('A') <= ord(inp[i]) < ord('a'):
        case_change = chr(ord(inp[i]) + diff)
    elif ord(inp[i]) >= ord('a'):
        case_change = chr(ord(inp[i]) - diff)
    else:
        case_change = inp[i]
    generate(inp, i + 1, out + case_change)


generate(inp, 0, "")
print("\n")


def generate2(inp, i, out):
    if i == len(inp):
        print(out, end=" ")
        return

    generate(inp, i + 1, out + inp[i].lower())
    generate(inp, i + 1, out + inp[i].upper())


generate2(inp, 0, "")
