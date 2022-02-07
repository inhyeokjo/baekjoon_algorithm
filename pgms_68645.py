# 프로그래머스 > 코딩테스트연습 > 원간 코드 챌린지 시즌1 > 삼각 달팽이
# URL : https://programmers.co.kr/learn/courses/30/lessons/68645

def solution(n):
    top_structure = [[0 for _ in range(i)] for i in range(1, n + 1)]
    make_tree(1, 1, n, 1, top_structure)
    answer = [element for sub_tree in top_structure for element in sub_tree]
    return answer


def make_tree(x, y, n, first_num, top_structure):
    if n <= 0:
        return
    for moving_x in range(x - 1, x + n - 1):
        top_structure[moving_x][y-1] = first_num
        first_num += 1
    for moving_y in range(y, y + n - 1):
        top_structure[moving_x][moving_y] = first_num
        first_num += 1
    while moving_x > x:
        moving_y -= 1
        moving_x -= 1
        top_structure[moving_x][moving_y] = first_num
        first_num += 1
    make_tree(x + 2, y + 1, n - 3, first_num, top_structure)


print(solution(1000))
