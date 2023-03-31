# https://www.geeksforgeeks.org/generate-all-binary-strings-from-given-pattern/

s = "1??0?101"
s_list = []


def insert_char(c, s_list):
    new_strings = []
    while s_list:
        if c == "?":
            s = s_list.pop()
            s1 = '0' + s
            s2 = '1' + s
            new_strings.extend([s1, s2])
        else:
            s = c + s_list.pop()
            new_strings.append(s)
    return new_strings


def generate(inp_str, s_list, i, n):
    if i == n:
        if s[n] != "?":
            s_list.append(s[n])
        else:
            s_list.append("0")
            s_list.append("1")
        return s_list

    # append s[n] to all items in s_list
    s_list = insert_char(inp_str[i], generate(inp_str, s_list, i + 1, n))
    return s_list


n = len(s) - 1
print(generate(s, s_list, 0, n))

