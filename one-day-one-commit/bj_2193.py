import sys
import math

def nCr(n, r):
    if r > n - r:
        r = n - r
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


input = sys.stdin.readline
n = int(input())
number_of_0 = n - 1
number_of_01 = 0

result = 0

while number_of_0 >= 0:
    result += nCr(number_of_01 + number_of_0, number_of_0)
    number_of_0 -= 2
    number_of_01 += 1
print(result)
