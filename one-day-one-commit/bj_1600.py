# import sys
# from collections import deque
#
#
# def make_board(x):
#     if x == '1':
#         return [-1] * (k + 1)
#     if x == '0':
#         return [40001] * (k + 1)
#
#
# def get_monkey_move(x, y, z):
#     monkey_moves = [(x - 1, y, z),
#                     (x, y + 1, z),
#                     (x + 1, y, z),
#                     (x, y - 1, z)]
#     possible_monkey_moves = []
#     for i, j, k in monkey_moves:
#         if can_move(i, j, k):
#             board[i][j][k] = board[x][y][z] + 1
#             visited[i][j][k] = True
#             possible_monkey_moves.append((i, j, k))
#     return possible_monkey_moves
#
#
# def get_horse_move(x, y, z):
#     horse_moves = [
#         (x - 2, y - 1, z - 1), (x - 1, y - 2, z - 1),
#         (x + 2, y - 1, z - 1), (x + 1, y - 2, z - 1),
#         (x - 2, y + 1, z - 1), (x - 1, y + 2, z - 1),
#         (x + 2, y + 1, z - 1), (x + 1, y + 2, z - 1)]
#     possible_horse_moves = []
#     for i, j, k in horse_moves:
#         if can_move(i, j, k):
#             board[i][j][k] = board[x][y][z] + 1
#             visited[i][j][k] = True
#             possible_horse_moves.append((i, j, k))
#     return possible_horse_moves
#
#
# def can_move(x, y, z):
#     return 0 <= min(x, y) \
#            and y < w \
#            and x < h \
#            and not visited[x][y][z] \
#            and board[x][y][z] != -1
#
#
# input = sys.stdin.readline
#
# k = int(input().strip())
# w, h = map(int, input().split())
#
# visited = [[[False] * (k + 1) for _ in range(w)] for _ in range(h)]
# board = [list(map(make_board, input().split())) for _ in range(h)]
#
# queue = deque([(0, 0, k)])
# board[0][0][k] = 0
# visited[0][0][k] = True
#
# result = -1
#
# while queue:
#     x, y, z = queue.popleft()
#     if (x, y) == (h - 1, w - 1):
#         result = board[x][y][z]
#         break
#     if z <= 0:
#         next_nodes = get_monkey_move(x, y, z)
#     else:
#         next_nodes = get_monkey_move(x, y, z) + get_horse_move(x, y, z)
#     queue.extend(next_nodes)
# print(result)

import sys
from collections import deque


def get_monkey_move(x, y, z):
    monkey_moves = [(x - 1, y, z),
                    (x, y + 1, z),
                    (x + 1, y, z),
                    (x, y - 1, z)]
    for i, j, k in monkey_moves:
        if can_move(i, j, k):
            visited[i][j][k] = visited[x][y][z] + 1
            queue.append((i, j, k))


def get_horse_move(x, y, z):
    horse_moves = [
        (x - 2, y - 1, z - 1), (x - 1, y - 2, z - 1),
        (x + 2, y - 1, z - 1), (x + 1, y - 2, z - 1),
        (x - 2, y + 1, z - 1), (x - 1, y + 2, z - 1),
        (x + 2, y + 1, z - 1), (x + 1, y + 2, z - 1)]
    for i, j, k in horse_moves:
        if can_move(i, j, k):
            visited[i][j][k] = visited[x][y][z] + 1
            queue.append((i, j, k))


def can_move(x, y, z):
    return 0 <= min(x, y) \
           and y < w \
           and x < h \
           and visited[x][y][z] == float('inf') \
           and board[x][y] != 1


input = sys.stdin.readline

k = int(input().strip())
w, h = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h)]

visited = [[[float('inf') for _ in range(k + 1)] for _ in range(w)] for _ in range(h)]

queue = deque([(0, 0, k)])
visited[0][0][k] = 0

result = -1

while queue:
    x, y, z = queue.popleft()
    if (x, y) == (h - 1, w - 1):
        result = visited[x][y][z]
        break
    if visited[x][y][z] != min(visited[x][y][z:]):
        continue
    get_monkey_move(x, y, z)
    if z > 0:
        get_horse_move(x, y, z)
print(result)
