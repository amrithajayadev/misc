# https://leetcode.com/problems/decode-ways/


def decode_ways(inp_str, i):
    if i == len(inp_str):
        return 1
    if inp_str[i] == '0':
        return 0
    # case where each string is processed individually
    count = decode_ways(inp_str, i + 1)

    # case where numbers can be concatenated, then we skip the next index because already accounted for.
    if i < len(inp_str) - 1 and (inp_str[i] == '1' or (inp_str[i] == '2' and inp_str[i + 1] < '7')):
        count += decode_ways(inp_str, i + 2)
    return count


count = 0
print(decode_ways("11106", 0))
print(count)