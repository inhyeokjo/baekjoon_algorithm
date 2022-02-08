import sys

input = sys.stdin.readline

max = int(input())
monetary_units = list(map(int, input().strip().split()))
monetary_units.reverse()

cache = [1 if i in monetary_units else 99999 for i in range(monetary_units[0] * 2)]
cache[0] = 0

no = False

for i in range(2, monetary_units[0] * 2):
    first = True
    for j in range(max):
        if i == monetary_units[j]:
            break
        if i > monetary_units[j]:
            if first:
                cache[i] = cache[i - monetary_units[j]] + 1
                first = False
                continue
            if cache[i - monetary_units[j]] + 1 < cache[i]:
                print('No')
                no = True
                break
    if no:
        break
if not no:
    print('Yes')
