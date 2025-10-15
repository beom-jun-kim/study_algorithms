# def find_max_occurred_alphabet(strings):
#     alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "o", "p", "q", "r", "s", "t", "u",
#                      "v", "w", "x", "y", "z"]
#     max_occurrences = 0
#     max_alphabet = alphabet_list[0]
#     for alphabet in alphabet_list:
#         occurrences = 0
#         for string in strings:
#             if alphabet == string:
#                 occurrences += 1
#         if occurrences > max_occurrences:
#             max_occurrences = occurrences
#             max_alphabet = alphabet
#
#     return max_alphabet

def find_max_occurred_alphabet(nums):
    alphabet_occurrence_array = [0] * 26

    for num in nums:
        if not num.isalpha():
            continue
        array_index = ord(num) - ord('a')
        alphabet_occurrence_array[array_index] += 1

    max_occurrence = 0
    max_alphabet_index = 0
    for index in range (len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]
        if alphabet_occurrence > max_occurrence:
            max_occurrence = alphabet_occurrence
            max_alphabet_index = index
    return chr(max_alphabet_index + ord('a'))


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
