import sys
from collections import defaultdict

my_list = defaultdict(list)
for i in range(int(sys.stdin.readline().strip())):
    a, b = map(int, sys.stdin.readline().strip().split())
    my_list[a].append(b)

for i in sorted(my_list.keys()):
    if len(my_list[i]) > 1:
        for j in sorted(my_list[i]):
            print(f"{i} {j}")
    else:
        print(f"{i} {my_list[i][0]}")
