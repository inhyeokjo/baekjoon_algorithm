import sys

input = sys.stdin.readline

people_number = int(input())
time_list = sorted(list(map(int, input().split())))
result = 0
for i in range(people_number):
    result += time_list[i]*(people_number-i)
print(result)

