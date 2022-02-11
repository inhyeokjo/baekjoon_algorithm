import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline


def get_number_of_case(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    return sum([get_case(board, 0, i) for i in range(len(board))])


def put_palace(board, line_index, position):
    for i in range(len(board)):
        board[i][position] += 1
        board[line_index][i] += 1
    board[line_index][position] -= 1
    if len(board) == 1:
        return
    for i in [line_index-1, line_index+1]:
        for j in [position-1, position+1]:
            if i < 0 or j < 0 or i >= len(board) or j >= len(board):
                continue
            board[i][j] += 1


def remove_palace(board, line_index, position):
    for i in range(len(board)):
        board[i][position] -= 1
        board[line_index][i] -= 1
    board[line_index][position] += 1
    if len(board) == 1:
        return
    for i in [line_index-1, line_index+1]:
        for j in [position-1, position+1]:
            if i < 0 or j < 0 or i >= len(board) or j >= len(board):
                continue
            board[i][j] -= 1


def get_case(board, line_index, position):
    if line_index == len(board) - 1:
        return 1
    put_palace(board, line_index, position)
    result = 0
    for i, line_position in enumerate(board[line_index+1]):
        if line_position == 0:
            result += get_case(board, line_index + 1, i)
    remove_palace(board, line_index, position)
    return result

def _get_case(board, line_index, position):
    for i in range(board):
        for j in range(board[i]):
            put_palace(board, i, j)


for _ in range(int(input())):
    print(get_number_of_case(int(input())) % 1000000007)
print(1)