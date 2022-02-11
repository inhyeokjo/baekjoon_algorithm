import sys

input = sys.stdin.readline

n, k = map(int, input().split())

target = 0
while k > 0:
    target += 1
    if n % target == 0:
        k -= 1
    if n < target/2:
        target = 0
        break
print(target)
