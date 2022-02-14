import sys

input = sys.stdin.readline

n = int(input())
target_order = list(map(int, input().split()))
shuffle = list(map(int, input().split()))

cards = [i for i in range(n)]
cards_to_player = list(map(lambda x: x % 3, cards))

start_cards_order = cards.copy()


def su(cards):
    return list(map(lambda x: shuffle[x], cards))


order = 0
cannot_trick = False
while cards_to_player != target_order:
    cards = su(cards)
    cards_to_player = list(map(lambda x: x % 3, cards))
    order += 1
    if cards == start_cards_order:
        cannot_trick = True
        break

if cannot_trick:
    print(-1)
else:
    print(order)
