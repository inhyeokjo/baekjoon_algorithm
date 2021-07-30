# 문제
# 베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.
#
# 이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.
#
# 예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)
#
# 자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오.
#
# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 케이스는 n을 포함하는 한 줄로 이루어져 있다.
#
# 입력의 마지막에는 0이 주어진다.
#
# 출력
# 각 테스트 케이스에 대해서, n보다 크고, 2n보다 작거나 같은 소수의 개수를 출력한다.
#
# 제한
# 1 ≤ n ≤ 123,456

# import sys
#
# prime_map_true_set = [2, 3]
# max_num = 3
#
#
# def make_map(n):
#     global max_num
#     prime_map_true_set.extend([i for i in range(max_num + 1, n + 1)])
#     for index_num in prime_map_true_set:
#         for j in list(set(range(index_num*2, n + 1, index_num)) & set(prime_map_true_set)):
#             prime_map_true_set.remove(j)
#         prime_map_true_set.sort()
#     max_num = n
#
#
# while True:
#     n = int(sys.stdin.readline().strip())
#     if not n:
#         break
#     if 2 * n > max_num:
#         make_map(2 * n)
#     print(sum(list([True for i in prime_map_true_set if n<i<=n*2])))


import sys

prime_map = [False, False, True, True]
max_num = 3


def make_map(n):
    global max_num
    prime_map.extend([True for _ in range(max_num + 1, n + 1)])
    index_num = -1
    for i in prime_map:
        index_num += 1
        if i:
            for j in range(max_num - (max_num % index_num), n+1, index_num):
                prime_map[j] = False
            prime_map[index_num] = True
    max_num = n


while True:
    n = int(sys.stdin.readline().strip())
    if not n:
        break
    if 2 * n > max_num:
        make_map(2 * n)
    print(sum(prime_map[n + 1:n * 2+1]))