import sys


class node:
    def __init__(self):
        self.depth = 0
        self.left = -1
        self.right = -1


def inorder(nodes, number, order, depth):
    global order_number
    if nodes[number].left != -1:
        inorder(nodes, nodes[number].left, order, depth + 1)
    order[depth].append(order_number)
    order_number += 1
    if nodes[number].right != -1:
        inorder(nodes, nodes[number].right, order, depth + 1)


input = sys.stdin.readline
n = int(input())
nodes = [node() for _ in range(n + 1)]
parent = [0] * (n + 1)
for _ in range(n):
    number, left, right = map(int, input().split())
    nodes[number].left = left
    nodes[number].right = right
    if left != -1:
        parent[left]

order_number = 1
order = [[] for _ in range(n + 1)]
inorder(nodes, 1, order, 1)

result = max(order[1]) - min(order[1]) + 1
level = 1
for i in range(1, len(order)):
    if order[i]:
        if result < max(order[i]) - min(order[i]) + 1:
            result = max(order[i]) - min(order[i]) + 1
            level = i
print(level, result)
