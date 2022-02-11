import sys

input = sys.stdin.readline

second_age = 0
first_age = 1
target = int(input())
if target == 0:
    print(0)
else:
    for _ in range(target - 1):
        now = second_age + first_age
        second_age = first_age
        first_age = now
    print(first_age)
