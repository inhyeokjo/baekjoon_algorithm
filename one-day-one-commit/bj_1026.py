import sys

input = sys.stdin.readline
depth = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(sum(map(lambda a: a[0] * a[1], zip(sorted(B), sorted(A, reverse=True)))))
