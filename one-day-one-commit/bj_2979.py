import sys

input = sys.stdin.readline

price = [0] + list(map(int, input().split()))
time_line = [0 for _ in range(101)]

for _ in range(3):
    start, end = map(int, input().split())
    for i in range(start, end):
        time_line[i] += 1
print(sum(map(lambda x: x * price[x], time_line)))
