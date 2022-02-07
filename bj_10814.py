from sys import stdin
from collections import defaultdict

my_dict = defaultdict(list)
for _ in range(int(stdin.readline().strip())):
    a, b = stdin.readline().strip().split()
    my_dict[int(a)].append(b)

for i in sorted(my_dict.keys()):
    for j in my_dict[i]:
        print(f"{i} {j}")