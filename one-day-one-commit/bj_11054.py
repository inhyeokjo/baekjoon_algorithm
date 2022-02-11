import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

board = [[0 if a[i] < a[j] else -1 for j in range(n)] for i in range(n)]


def check_indirect_path(board, i, j, plus):
    if i < j:
        if board[i][i + plus] != -1 and board[i + plus][j] != -1:
            board[i][j] = max(board[i][j], board[i][i + plus] + board[i + plus][j] + 1)
    if i > j:
        if board[i][j + plus] != -1 and board[j + plus][j] != -1:
            board[i][j] = max(board[i][j], board[i][j + plus] + board[j + plus][j] + 1)
    if i == j:
        return


for distance_from_diagonal in range(2, n):
    for i in range(n - distance_from_diagonal):
        j = i + distance_from_diagonal
        for plus in range(1, j - i):
            check_indirect_path(board, i, j, plus)
            check_indirect_path(board, j, i, plus)


result = 0
for j in range(1, n-1):
    line_up = []
    line_down = []
    for i in range(n):
        if i < j:
            line_up.append(board[i][j])
        if j < i:
            line_down.append(board[i][j])
    this_line_max = max(line_up)+max(line_down)+3
    result = max(this_line_max, result)

print(result)
