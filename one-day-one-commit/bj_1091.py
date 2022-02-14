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
