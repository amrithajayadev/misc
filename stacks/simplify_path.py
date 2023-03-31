# https://leetcode.com/problems/simplify-path/description/
def simplifyPath(path: str) -> str:
    filenames = path.split("/")
    stack = []

    for file in filenames:
        if file == "..":
            if stack:
                stack.pop()
        elif file == ".":
            continue
        elif len(file) == 0:
            continue
        else:
            stack.append(file)

    out = "/".join(stack)
    if len(out) > 1:
        return "/" + out
    else:
        return "/"
