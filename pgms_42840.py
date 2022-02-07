def solution(answers):
    man1_style = [1, 2, 3, 4, 5] * 2001
    man2_style = [2, 1, 2, 3, 2, 4, 2, 5] * 2001
    man3_style = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1001

    man1_score = 0
    man2_score = 0
    man3_score = 0

    for i in range(len(answers)):
        man1_score += answers[i] == man1_style[i]
        man2_score += answers[i] == man2_style[i]
        man3_score += answers[i] == man3_style[i]

    who = [man1_score, man2_score, man3_score]

    answer = [x+1 for x in range(3) if max(who) == who[x]]
    return answer

print(solution([1,3,2,4,2]))