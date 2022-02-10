import sys

sys.setrecursionlimit(1000000)


class node:
    def __init__(self):
        self.left = -1
        self.right = -1
        self.depth = 0
        self.order = 0


def inorder(nodes, number, order, depth):
    global order_number
    if nodes[number].left != -1:
        inorder(nodes, nodes[number].left, order, depth + 1)
    order[depth].append(order_number)
    order_number += 1
    if nodes[number].right != -1:
        inorder(nodes, nodes[number].right, order, depth + 1)


n = int(sys.stdin.readline())
a = [node() for _ in range(10001)]
left = [0] * 10001
right = [0] * 10001
parent = [0] * 10001
order = 0

for i in range(n):
    x, b, c = map(int, sys.stdin.readline().split())
    a[x].left = b
    a[x].right = c
    if b != -1:
        parent[b] += 1
    if c != -1:
        parent[c] += 1

root = 0
for i in range(1, n + 1):
    if parent[i] == 0:
        root = i

order_number = 1
order = [[] for _ in range(n + 1)]
inorder(a, root, order, 1)

result = max(order[1]) - min(order[1]) + 1
level = 1
for i in range(1, len(order)):
    if order[i]:
        if result < max(order[i]) - min(order[i]) + 1:
            result = max(order[i]) - min(order[i]) + 1
            level = i
print(level, result)
