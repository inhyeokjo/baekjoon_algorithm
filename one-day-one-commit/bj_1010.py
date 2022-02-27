import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    m, n = map(int, input().split())
    result = math.factorial(n)//math.factorial(n-m)//math.factorial(m)
    print(result)