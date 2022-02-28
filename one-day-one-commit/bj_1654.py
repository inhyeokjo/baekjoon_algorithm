import sys

input = sys.stdin.readline

k, n = map(int, input().split())
k_length = [int(input().strip()) for _ in range(k)]
min_length = 1
max_length = sum(k_length) // n

while min_length <= max_length:
    mid = (min_length + max_length) // 2
    cnt = sum(map(lambda x: x // mid, k_length))
    if cnt >= n:
        min_length = mid + 1
    else:
        max_length = mid - 1
print(max_length)
