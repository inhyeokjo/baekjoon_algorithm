# 문제
# 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.
#
# 입력
# 세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.
#
# 출력
# 직사각형의 네 번째 점의 좌표를 출력한다.

point = []
for _ in range(3):
    p = list(map(int, input().strip().split()))
    point.append(p)
x_point, y_point = zip(point[0], point[1], point[2])

for i in [1, 2]:
    if x_point[i] == x_point[0]:
        if i - 1:
            x = x_point[1]
        else:
            x = x_point[2]
        break
    if i == 2:
        x = x_point[0]
for i in [1, 2]:
    if y_point[i] == y_point[0]:
        if i - 1:
            y = y_point[1]
        else:
            y = y_point[2]
        break
    if i == 2:
        y = y_point[0]

print(x, y)
