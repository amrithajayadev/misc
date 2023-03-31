from collections import Counter


def checkIfPangram(sentence: str) -> bool:
    if len(sentence) < 26:
        return False
    alphabets = {chr(k) for k in range(ord('a'), ord('z') + 1)}

    freq_map = Counter(sentence)
    for c in alphabets:
        if c not in freq_map:
            return False
    return True


sentence = "thequickbrownfoxjumpsoverthelazydog"
if checkIfPangram(sentence):
    print("true")
else:
    print("false")


def check_pangram(sentence):
    seen = set(sentence)
    return len(seen) == 26

if check_pangram(sentence):
    print("true")
else:
    print("false")