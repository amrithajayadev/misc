# https://www.geeksforgeeks.org/find-largest-word-dictionary-deleting-characters-given-string/

# dictionary = {"ale", "applepie", "monkey", "plea"}
# str1 = "abpcplea"

dictionary = {"pintu", "geeksfor", "geeksgeeks",
              " forgeek"}
str1 = "geeksforgeeks"


def largest_word_in_dict_and_input2(str1, dictionary):
    char_count_str1 = {}
    for c in str1:
        if c in char_count_str1:
            char_count_str1[c] += 1
        else:
            char_count_str1[c] = 1
    large_word = ""
    for word in dictionary:
        word_in_str = True
        for ch in word:
            if ch not in char_count_str1:
                word_in_str = False
                break
        if word_in_str:
            large_word = word if len(word) > len(large_word) else large_word
    print(large_word)


largest_word_in_dict_and_input2(str1, dictionary)
