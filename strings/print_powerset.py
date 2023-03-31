str1 = "aabc"

output = []


def generate(inp, i, curr, output):
    if i == len(inp):
        output.append(curr)
        return output
    if curr not in output:
        generate(inp, i + 1, curr + inp[i], output)
        generate(inp, i + 1, curr, output)


generate(str1, 0, "", output)
print(output)

# if input string has duplicate chars, then this will generate some subsets twice.
def generate_dupl(inp, i, curr):
    if i == len(inp):
        print(curr, end=" ")
        return
    generate_dupl(inp, i + 1, curr + inp[i])
    generate_dupl(inp, i + 1, curr)


generate_dupl(str1, 0, "")
