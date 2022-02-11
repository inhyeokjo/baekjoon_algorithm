import sys

input = sys.stdin.readline

ends = [0] + [(i + 1) * i // 2 for i in range(1, 46)]
start, end = map(int, input().split())

skip_value = 0
for i in range(len(ends)):
    if ends[i] >= start - 1:
        skip_value += i * (start - 1 - ends[i - 1])
        break
    skip_value += i ** 2

sum_value = 0
for i in range(len(ends)):
    if ends[i] >= end:
        sum_value += i * (end - ends[i - 1])
        break
    sum_value += i ** 2
print(sum_value-skip_value)
