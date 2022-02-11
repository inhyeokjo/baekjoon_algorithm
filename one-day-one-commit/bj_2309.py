import sys

input = sys.stdin.readline

small_9 = [int(input()) for _ in range(9)]
over_tall = sum(small_9) - 100
for man in small_9:
    if over_tall == man*2:
        continue
    if over_tall-man in small_9:
        small_9.remove(man)
        small_9.remove(over_tall-man)
        break
for i in sorted(small_9):
    print(i)