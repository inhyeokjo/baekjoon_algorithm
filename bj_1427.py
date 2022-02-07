import sys

l = sorted(list(sys.stdin.readline().strip()))[::-1]
print("".join(l))
