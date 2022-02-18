import sys

input = sys.stdin.readline

n, k = map(int, input().split())
word_list = [set(input()) for _ in range(n)]


def get_possible_word(selected_words):
    map(lambda x: x-selected_words, maintain_words)


def f(max_depth, depth, maintain_words_list, node, selected_words):
    if depth == max_depth:
        return get_possible_word()
    max_number = 0
    for maintain_word in maintain_words_list:
        possible_word = f(max_depth, depth + 1, maintain_words_list.copy(), maintain_word, selected_words)
        max_number = max(max_number, possible_word)
    return max_number

if k < 5:
    print(0)
else:
    k -= 5
    maintain_words = list(map(lambda x: x - set('aicnt'), word_list))
    maintain_words_set = set(''.join(maintain_words))
    f()
