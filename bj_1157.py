# 문제
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
#
# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
#
# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.


# alp = {chr(i):0 for i in range(ord('A'), ord('Z')+1)}
s=list(input().upper())
alp_num = [0 for i in range(ord('A')+ord('Z')+1)]
for i in s:
    alp_num[ord(i)-ord('A')] +=1
val = max(alp_num)
ind = alp_num.index(val)
alp_num.pop(ind)
if max(alp_num) == val:
    print('?')
else:
    print(chr(ind+ord('A')))