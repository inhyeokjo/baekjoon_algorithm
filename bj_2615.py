import sys

board = [list(sys.stdin.readline().strip().split()) for _ in range(19)]


def next_stone(x, y, color):
    if has_horizontal_answer(color, x, y):
        if x >= 13 and board[x + 5][y] == color:
            return False
        print_result(color, x, y)
        return True
    if has_vertical_answer(color, x, y):
        if y >= 13 and board[x][y + 5] == color:
            return False
        print_result(color, x, y)
        return True
    if has_diagonal_answer(color, x, y):
        if x >= 13 and y >= 13 and board[x + 5][y + 5] == color:
            return False
        print_result(color, x, y)
        return True
    return False


def has_horizontal_answer(color, x, y):
    return x <= 14 and board[x + 1][y] == color and board[x + 2][y] == color and board[x + 3][y] == color and \
           board[x + 4][y] == color


def has_vertical_answer(color, x, y):
    return y <= 14 and board[x][y + 1] == color and board[x][y + 2] == color and board[x][y + 3] == color and board[x][
        y + 4] == color


def has_diagonal_answer(color, x, y):
    return x <= 14 and y <= 14 and board[x + 1][y + 1] == color and board[x + 2][y + 2] == color and board[x + 3][
        y + 3] == color and board[x + 4][y + 4] == color


def print_result(color, x, y):
    print(color)
    print(f"{x + 1} {y + 1}")


game_end = False
for x in range(19):
    for y in range(19):
        if board[x][y] != '0':
            color = board[x][y]
            if next_stone(x, y, color):
                game_end = True
                break
    if game_end:
        break
if not game_end:
    print(0)
