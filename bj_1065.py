# 문제
# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.
#
# 출력
# 첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

def find(n):
    total_num = 0
    for i in range(1, n+1):
        break_point = False
        if len(str(i)) <= 2:
            total_num += 1
            continue
        else:
            num_list = list(map(int, list(str(i))))
            tolerance = num_list[1]-num_list[0]
            last_num = num_list[1]
            for j in num_list[2:]:
                if tolerance != j-last_num:
                    break_point = True
                    break
                last_num = j
            if break_point:
                continue
            else:
                total_num += 1
    return total_num


n = int(input())
print(find(n))