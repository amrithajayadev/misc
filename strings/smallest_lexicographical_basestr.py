# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

def smallestEquivalentString(s1: str, s2: str, baseStr: str) -> str:
    char_map = {c: set() for c in s1 + s2}
    out = []
    for c1, c2 in zip(s1, s2):
        char_map[c1].add(c2)
        char_map[c2].add(c1)
    print(char_map)
    for c in baseStr:
        if c > min(char_map.get(c, c)):
            out.append(min(char_map[c]))
        else:
            out.append(c)
    return ''.join(out)


s1 = "parker"
s2 = "morris"
baseStr = "parser"

# s1 = "hello"
# s2 = "world"
# baseStr = "hold"

# s1 = "leetcode"
# s2 = "programs"
# baseStr = "sourcecode"

o = smallestEquivalentString(s1, s2, baseStr)
print(o)
