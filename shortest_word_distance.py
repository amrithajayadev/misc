words = ["practice", "makes", "perfect", "coding", "makes"]
# word1 = "coding"
# word2 = "practice" #3

word1 = "makes"
word2 = "coding" # 1


def find_shortest_distance(words, word1, word2):
    w1 = float('-inf')
    w2 = float('inf')
    d = len(words) + 1
    for i, w in enumerate(words):
        if w == word1:
            w1 = i
        elif w == word2:
            w2 = i
        d = min(d, abs(w1 - w2))
        print(w1, w2)
    return d


print(find_shortest_distance(words, word1, word2))