# 문제
# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.
#
# 입력
# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
#
# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
#
# 출력
# 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.

import sys


for i in range(int(input())):
    num_score_list = list(map(int, sys.stdin.readline().strip().split()))
    num = num_score_list[0]
    score_list = num_score_list[1:]
    mean = sum(score_list)/num
    count = 0
    for i in score_list:
        if i > mean:
            count +=1
    rate = count/num*100
    print(f"{rate:.3f}%")