import sys

input = sys.stdin.readline

all_word = list(map(set, zip(*[input().strip() for _ in range(int(input()))])))
result = ''.join([i.pop() if len(i) == 1 else '?' for i in all_word])
print(result)