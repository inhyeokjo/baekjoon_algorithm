import copy
import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline

horizontal_result_board = [list(map(int, input().split())) for _ in range(9)]
vertical_result_board = list(map(list, zip(*horizontal_result_board)))
box_result_board = [[horizontal_result_board[j // 3 + i // 3 * 3][j % 3 + i % 3 * 3] for j in range(9)] for i in
                    range(9)]
unconfirmed_index = []
candidate_board = [
    [set([1, 2, 3, 4, 5, 6, 7, 8, 9]) if horizontal_result_board[i][j] == 0 else set() for j in range(9)] for i in
    range(9)]


def back_tracing(i):
    global candidate_board
    if len(unconfirmed_index) == i:
        return True
    if not unconfirmed_index[i]:
        return False
    target_index = unconfirmed_index[i]
    candidate_board_copy = copy.deepcopy(candidate_board)
    for candidate in candidate_board[target_index[0]][target_index[1]].copy():
        confirm_number(*target_index, candidate)
        if back_tracing(i + 1):
            return True
        else:
            candidate_board = candidate_board_copy
            confirm_number(target_index[0], target_index[1], 0)
            continue
    return False


def update_candidate(i, j):
    for a in range(9):
        candidate_board[i][a] -= {horizontal_result_board[i][j]}
        candidate_board[a][j] -= {horizontal_result_board[i][j]}
        candidate_board[i // 3 * 3 + a // 3][j // 3 * 3 + a % 3] -= {horizontal_result_board[i][j]}


def confirm_number(i, j, number):
    horizontal_result_board[i][j] = number
    vertical_result_board[j][i] = number
    box_result_board[j // 3 + i // 3 * 3][j % 3 + i % 3 * 3] = number
    if number != 0:
        update_candidate(i, j)


for i in range(9):
    for j in range(9):
        if horizontal_result_board[i][j] != 0:
            continue
        candidate_board[i][j] -= set(horizontal_result_board[i])
        candidate_board[i][j] -= set(vertical_result_board[j])
        candidate_board[i][j] -= set(box_result_board[j // 3 + i // 3 * 3])
        if len(candidate_board[i][j]) == 1:
            confirm_number(i, j, candidate_board[i][j].pop())
        else:
            unconfirmed_index.append([i, j])
back_tracing(0)
print('\n'.join(list(map(lambda x: ' '.join(list(map(str, x))), horizontal_result_board))))
