import sys

stack = []


def process(command, number):
    if command == "push":
        stack.append(number)
    if command == "pop":
        print(stack.pop() if len(stack) > 0 else -1)
    if command == "size":
        print(len(stack))
    if command == "empty":
        print(1 if len(stack) == 0 else 0)
    if command == "top":
        print(stack[-1] if len(stack) > 0 else -1)

for _ in range(int(sys.stdin.readline().strip())):
    split = sys.stdin.readline().strip().split()
    split.append('0')
    process(split[0], split[1])