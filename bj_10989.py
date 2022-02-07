import sys

array = [0]*10001

for _ in range(int(sys.stdin.readline().strip())):
    array[int(sys.stdin.readline().strip())] += 1

for n in range(1, len(array)):
    if not array[n]:
        continue
    for _ in range(array[n]):
        print(n)
