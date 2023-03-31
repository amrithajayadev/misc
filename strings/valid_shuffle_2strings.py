# s1 = "XYYZ"
# s2 = "ABCC"
# "ZXYYCCCA"

s1 = "XY"
s2  = "12"
# 1XY2
# 1XX2
def check_valid_shuffle(s1, s2, x):
    temp = s1 + s2
    ret1 = ret2 = True
    if len(temp) != len(x):
        return False
    for i, c in enumerate(x):
        if c not in temp:
            ret1 = False
    for i, c in enumerate(temp):
        if c not in x:
            ret2 = False

    return ret1 and ret2


if check_valid_shuffle(s1, s2, "1XX2"):
    print("True")
else:
    print("False")
