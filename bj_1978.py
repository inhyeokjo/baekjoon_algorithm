# 문제
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.
#
# 출력
# 주어진 수들 중 소수의 개수를 출력한다.

sosu = [2]
for i in range(3, 1001):
    break_value = False
    for j in sosu:
        if i % j == 0:
            break_value = True
            break
    if break_value:
        continue
    sosu.append(i)

input()
count = 0
for i in map(int, input().split()):
    if i in sosu:
        count += 1
print(count)
