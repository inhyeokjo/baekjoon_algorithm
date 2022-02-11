a, b = map(int, input().split())
if a < b:
    a, b = b, a
x, y = a, b
while x % y != 0:
    x, y = y, x % y
print(y)
print(a*b//y)
