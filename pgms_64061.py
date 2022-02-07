def solution(board, moves):
    basket = []
    answer = 0
    board = list(map(list, list(zip(*board))))
    for i in board:
        i.reverse()
    board = [[j for j in i if j != 0] for i in board]

    for move in moves:
        move -= 1
        if len(board[move]):
            basket.append(board[move].pop())
        if len(basket) >= 2 and basket[-1] == basket[-2]:
            basket = basket[0:-2]
            answer += 2
    return answer

