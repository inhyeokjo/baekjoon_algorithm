from sys import stdin
from collections import defaultdict

my_dict = defaultdict(set)
for i in range(int(stdin.readline().strip())):
    world = stdin.readline().strip()
    my_dict[len(world)].add(world)

for i in sorted(my_dict.keys()):
    for j in sorted(list(my_dict[i])):
        print(j)
