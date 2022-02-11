import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    order = 0
    answer = []
    while n > 0:
        if n % 2 == 1:
            answer.append(str(order))
        n //= 2
        order += 1
    print(" ".join(answer))

