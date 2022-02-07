answer = []
num = int(input("변환하고싶은 10진수를 입력해주세요."))
while num:
    answer.append(str(num % 2))
    num //= 2

answer.reverse()
print("".join(answer))
