import sys
input = sys.stdin.readline

n = int(input())
fibo_list = [1, 0]
for _ in range(n):
    fibo_list = [sum(fibo_list) % 15746, fibo_list[0]]
print(fibo_list[0])
