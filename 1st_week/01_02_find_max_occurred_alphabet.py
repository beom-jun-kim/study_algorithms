def find_max_occurred_alphabet(strings):
    alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "o", "p", "q", "r", "s", "t", "u",
                     "v", "w", "x", "y", "z"]
    max_occurrences = 0
    max_alphabet = alphabet_list[0]
    for alphabet in alphabet_list:
        occurrences = 0
        for string in strings:
            if alphabet == string:
                occurrences += 1
        if occurrences > max_occurrences:
            max_occurrences = occurrences
            max_alphabet = alphabet

    return max_alphabet


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
# print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
# print("정답 = b 현재 풀이 값 =", result("best of best youtube"))
