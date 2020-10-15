def remove(s1, s2):
    s1_l = list(s1)
    s2_l = list(s2)
    for c in s2_l:
        for c2 in s1_l:
            if c == c2:
                s1_l.pop(s1_l.index(c))

    removed = ''.join(s1_l)
    return removed

# s1='geeksforgeeks'
# s2='mask'

# s1= 'removeccharaterfrom'
# s2='string'

s1='counttakesandchecktakesso'
s2='halves'
print(remove(s1,s2))