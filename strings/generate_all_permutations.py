def insert_char_at_all_positions(char, perm_list):
    res = []
    for perm in perm_list:
        n = len(perm)
        for i in range(n + 1):
            new_perm = perm[:i] + char + perm[i:]
            if new_perm not in res:
                res.append(new_perm)
    return res


def generate_all_permutations(str1, n):
    if n == 0:
        return [str1[n]]
    p = insert_char_at_all_positions(str1[n], generate_all_permutations(str1, n - 1))
    return p


all_perm = generate_all_permutations('abcdd', len('abcdd') - 1)
print(all_perm)
print(len(all_perm))

# recursively find the permutations for bigger inputs.
# we start with a P(a) = [a]
# P(ab) = [ab, ba]
# P(abc) = [cab, acb, abc] + [cba, bca, bac]
# P(n) = Generate strings by appending the nth char at all positions of P(n-1)
