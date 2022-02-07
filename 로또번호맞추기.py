import random

random_num = [random.randint(1, 20) for _ in range(6)]

my_num = []
score = 0
print("1~20중 6가지 숫자를 생각하세요")
for i in range(6):
    my_num.append(int(input(f"{i + 1}번째 숫자를 적어주세요 >>")))
    if my_num[-1] in random_num:
        score +=1
print(f"정답은 {random_num}였습니다.")
print(f"당신은 {score}개 맞았습니다. 멍청하시네요.")