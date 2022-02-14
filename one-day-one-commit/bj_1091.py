import sys

input = sys.stdin.readline

n = int(input())
cards = [i for i in range(n)]
target_order = list(map(int, input().split()))
shuffle = list(map(int, input().split()))
can_joke = True

card_rotations = [[] for _ in range(n)]
for i, card_rotation in enumerate(card_rotations):
    card_rotation.append(cards[i])
    while True:
        next_card = shuffle[card_rotation[-1]]
        if next_card in card_rotation:
            circle_start_index = card_rotation.index(shuffle[card_rotation[-1]])
            card_rotation = list(map(lambda x: x % 3, card_rotation))
            not_circle_part = card_rotation[:circle_start_index]
            circle_part = card_rotation[circle_start_index:]
            card_rotation = [not_circle_part, circle_part]
            card_rotations[i] = card_rotation
            break
        card_rotation.append(next_card)

max_circle_start = max([len(card_rotation[0]) for card_rotation in card_rotations])
circle_size_set = set()
for i in card_rotations:
    circle_size_set.add(len(i[1]))
max_shuffle = eval('*'.join(map(str, circle_size_set))) + max_circle_start

indexes = [[-1] + [i for i, rotation in enumerate(card_rotation[0]) if rotation == target_order[i]] for i, card_rotation
           in
           enumerate(card_rotations)]
for card_number, card_rotation in enumerate(card_rotations):
    circle_matched_indexes = [i for i, rotation in enumerate(card_rotation[1]) if rotation == target_order[card_number]]
    if not circle_matched_indexes:
        can_joke = False
        break
    j = 0
    while indexes[card_number][-1] <= max_shuffle:
        indexes[card_number].extend(list(map(lambda x: x + len(card_rotation[1]) * j, circle_matched_indexes)))
        j += 1

result = -1
if can_joke:
    alive_indexes = set(indexes[0][1:])
    for index in indexes[1:]:
        alive_indexes = alive_indexes & set(index[1:])
        if len(alive_indexes) == 0:
            alive_indexes.add(-1)
            break
    result = min(list(alive_indexes))
print(result)

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# cards = [i for i in range(n)]
# p = list(map(int, input().split()))
# s = list(map(int, input().split()))
#
#
# def make_forward(cards):
#     max_circle_start = 0
#     forward = [[] for _ in range(n)]
#     for i in range(n):
#         forward[i].append(cards[i])
#         while True:
#             if s[forward[i][-1]] in forward[i]:
#                 forward[i].append(forward[i].index(s[forward[i][-1]]))
#                 break
#             forward[i].append(s[forward[i][-1]])
#         forward[i] = list(map(lambda x: x%3, forward[i][:-1]))+[forward[i][-1]]
#         forward[i] = [forward[i][:forward[i][-1]],forward[i][forward[i][-1]:forward[i][-2]]]
#         max_circle_start = max(max_circle_start, forward[i][-1])
#     return forward, max_circle_start
#
#
# def validation_check(cards):
#     for i, card in enumerate(cards):
#         if card % 3 != p[i]:
#             return False
#     return True
#
#
# def can_change_cards(forward):
#     for i, card_forward in enumerate(forward):
#         if p[i] not in card_forward:
#             return False
#     return True
#
#
#
#
# forward, max_circle_start = make_forward(cards)
#
# circle_size_set = set()
# for i in forward:
#     circle_size_set.add(len(i)-1-i[-1])
#
# max_repeat = eval('*'.join(map(str, circle_size_set))) + max_circle_start
#
# for i in forward:
#     while i[-1] <= max_repeat:
#
#
# while True:
#     if not can_change_cards(forward):
#         order = -1
#         break
#
# print()
