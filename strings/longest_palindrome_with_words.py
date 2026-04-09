def longestPalindrome(words):
    """
    :type words: List[str]
    :rtype: int
    Create a hashmap to store the words that have a palindrome.
    The longer palindrome can be created only for the words that have palindrome.
    1. case where two different
    2. case where same letter
    3. How to handle cases like [ab, ab, ab, ba, ba, ba, ll, ll] ->
    freq_map = {
        ab : 3
        ba : 2
        gg : 1
    }
    pal_map = { -> Optimisation
        "ab": "ba",
        "ba": "ab"
    }
    Iterate through freq_map,
    check if reverse exists in freq map.
    If exists, then add min(word, rev-word)*2 to res
    """

    def reverse(word):

        if word[0] == word[1]:
            return word
        rev = []
        for i in range(len(word) - 1, -1, -1):
            rev.append(word[i])
        return "".join(rev)

    res = 0
    freq_map = {}
    single_word_palindrome = False
    for word in words:
        freq_map[word] = 1 + freq_map.get(word, 0)

    for w in freq_map:
        rev = reverse(w)
        if rev == w:
            print(f"Processing w: {w}")
            if freq_map[w] == 1:
                if single_word_palindrome:
                    continue
                print(f"Processing w: {w}, single_word_palindrome:{single_word_palindrome}")
                single_word_palindrome = True
                res = res + (len(w) * freq_map[w])
                print(f"res={res}")
            else:
                res = res + (len(w) * freq_map[w])
                print(f"single_word_palindrome:{single_word_palindrome}, res={res}")
        elif rev in freq_map:
            res += min(freq_map[w], freq_map[rev]) * len(w)
            print(f"w:{w}, rev:{rev}, res={res}")
    return res

words = ["cc", "ll", "gg"]
longestPalindrome(words)