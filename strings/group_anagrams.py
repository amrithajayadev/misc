def group_anagrams(strs):
    a_dict = {}
    for s in strs:
        t = tuple(sorted(s))
        if t in a_dict:
            a_dict[t].append(s)
        else:
            a_dict[t] = [s]

    print(a_dict.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
group_anagrams(strs)