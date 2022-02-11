import sys

input = sys.stdin.readline

people = 0
max_people = 0
for _ in range(10):
    down, up = map(int, input().split())
    change = up - down
    people += change
    if max_people < people:
        max_people = people
print(max_people)
