# A Program to check if strings are rotations of each other or not

s1 = "abcd"
s2 = "cdab"


def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    temp = s1 + s1
    if s2 in temp:
        return True
    else:
        return False


if is_rotation("abcd", "cdab"):
    print("True")
else:
    print("False")
